import streamlit as st
import graphviz
from models.aturan_model import get_all_aturan

def show():
    # Halaman Chart Tree 
    st.title("Pohon Keputusan Rekomendasi Jurusan")

    # Contoh data riwayat
    data_riwayat = ["F2", "F19", "F4", "F14", "F3", "F8", None, None, None, "F28", None, "F36"]

    # Generate pohon
    dot = generate_tree(data_riwayat)

    # Tampilkan pohon (misalnya di Streamlit)
    st.graphviz_chart(dot)

def generate_tree(data_riwayat):
    dot = graphviz.Digraph()

    # Root
    dot.node("root", "Rekomendasi Jurusan\nKuliah di STMIKPLK")

    # Ambil data aturan
    df_aturan = get_all_aturan()

    # Debug: Tampilkan isi df_aturan untuk memastikan data diambil dengan benar
    # print("Data aturan dari database:")
    # print(df_aturan)

    # Jika df_aturan kosong, tambahkan pesan error di pohon
    if df_aturan.empty:
        dot.node("error", "Data aturan kosong", shape="box", style="filled", color="red")
        return dot

    # Kelompokkan kriteria berdasarkan jurusan
    grouped_by_jurusan = df_aturan.groupby('kode_jurusan')

    # Set untuk menyimpan node yang sudah ditambahkan
    added_nodes = {"root"}

    # Tentukan cabang utama berdasarkan jenjang (S1 atau D3)
    jurusan_info = {
        "J1": ("F1", "S1", "lightblue"),  # Teknik Informatika
        "J2": ("F1", "S1", "lightgreen"),  # Sistem Informasi
        "J3": ("F30", "D3", "lightcoral")  # Manajemen Informatika
    }

    # Tambahkan cabang utama (F1 untuk S1, F30 untuk D3)
    jenjang_nodes = {}
    for kode_jurusan, (parent_node, jenjang, color) in jurusan_info.items():
        if parent_node not in added_nodes:
            dot.node(parent_node, f"{parent_node} ({jenjang})")
            dot.edge("root", parent_node)
            added_nodes.add(parent_node)
        jenjang_nodes[kode_jurusan] = parent_node

    # Fungsi untuk menambahkan jalur berdasarkan node yang ada di data_riwayat
    def add_path(nodes_list, parent_node, jurusan_node, jurusan_name, color):
        previous_node = parent_node
        # Urutkan nodes_list berdasarkan kode_kriteria untuk konsistensi
        nodes_list = sorted(nodes_list, key=lambda x: x if x else "")
        for node in nodes_list:
            if node and node in data_riwayat and node not in added_nodes:  # Tambahkan hanya jika node ada di data_riwayat
                # Gunakan kode_kriteria sebagai label (seperti versi manual)
                dot.node(node, node)
                dot.edge(previous_node, node)
                added_nodes.add(node)
                previous_node = node
        # Jika ada node terakhir yang terhubung, tambahkan jurusan
        if previous_node != parent_node:
            dot.node(jurusan_node, jurusan_name, shape="box", style="filled", color=color)
            dot.edge(previous_node, jurusan_node)
            added_nodes.add(jurusan_node)
        else:
            # Jika tidak ada node yang ditambahkan, tetap tambahkan jurusan dengan status "tidak ada jalur"
            dot.node(jurusan_node, jurusan_name + "\n(Tidak ada jalur)", shape="box", style="filled", color=color)
            dot.edge(parent_node, jurusan_node)
            added_nodes.add(jurusan_node)

    # Iterasi melalui setiap jurusan
    for kode_jurusan, group in grouped_by_jurusan:
        if kode_jurusan not in jurusan_info:
            continue  # Skip jika jurusan tidak dikenal

        # Ambil parent node (F1 atau F30) dan informasi lainnya
        parent_node, jenjang, color = jurusan_info[kode_jurusan]
        jurusan_name = group['nama_jurusan'].iloc[0]  # Nama jurusan dari database
        nodes_list = group['kode_kriteria'].tolist()  # Daftar kode_kriteria untuk jurusan ini

        # Debug: Tampilkan nodes_list untuk setiap jurusan
        # print(f"Nodes untuk jurusan {kode_jurusan}: {nodes_list}")

        # Tambahkan jalur untuk jurusan ini
        add_path(nodes_list, parent_node, kode_jurusan, jurusan_name, color)

    # Debug: Tampilkan semua node yang ditambahkan
    # print(f"Semua node yang ditambahkan: {added_nodes}")

    # Jika tidak ada jalur yang cocok dengan data_riwayat, tambahkan pesan
    if len(added_nodes) <= len(jurusan_info) + 1:  # Hanya root dan cabang utama
        dot.node("no_path", "Tidak ada jalur yang cocok", shape="box", style="filled", color="yellow")
        dot.edge("root", "no_path")

    return dot