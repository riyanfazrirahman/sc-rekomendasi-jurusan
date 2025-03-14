import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from models.rekomendasi_model import get_relations, get_recommendation
from models.kriteria_model import get_options_kriteria

# Halaman Home
st.title("🎓 Sistem Rekomendasi Jurusan dengan Probabilitas")
st.markdown("---")

st.subheader("📌 Pilih Kriteria Kamu")

# Input kriteria dari user
kriteria_list = get_options_kriteria()
kriteria_user = st.multiselect("Pilih kriteria yang sesuai dengan kamu:", kriteria_list)

# Tombol rekomendasi
tombol_rekomendasi = st.button("🔍 Dapatkan Rekomendasi")
if tombol_rekomendasi:
    if kriteria_user:
        hasil_rekomendasi = get_recommendation(kriteria_user)
        
        if hasil_rekomendasi:
            st.markdown("### 📊 Hasil Rekomendasi")
            for jurusan, persen in sorted(hasil_rekomendasi.items(), key=lambda x: x[1], reverse=True):
                st.progress(persen / 100)
                st.write(f"**{jurusan}: {persen:.2f}%**")

            # Menampilkan Graph dengan streamlit-agraph
            st.markdown("### 🔗 Diagram Hubungan Kriteria & Jurusan")

            # Ambil hanya relasi yang berkaitan dengan `kriteria_user`
            relations = get_relations()
            relations_filtered = [(k, j) for k, j in relations if k in kriteria_user]

            # Buat node untuk kriteria yang dipilih
            nodes = [
                Node(id=kriteria, label=kriteria, size=20, color="#95a5a6")  # Abu-abu
                for kriteria in kriteria_user
            ]

            # Daftar warna untuk jurusan (biar tidak terlalu sedikit)
            daftar_warna = [
                "blue", "red", "purple", "brown", "orange", "pink", "cyan", "green", "yellow"
            ]
            warna_jurusan = {jurusan: daftar_warna[i % len(daftar_warna)]
                             for i, jurusan in enumerate(hasil_rekomendasi.keys())}

            # Cari nilai maksimum untuk normalisasi ukuran node
            max_persen = max(hasil_rekomendasi.values()) if hasil_rekomendasi else 1  

            # Node untuk jurusan yang direkomendasikan
            nodes += [
                Node(
                    id=jurusan,
                    label=f"{jurusan} ({persen:.2f}%)",
                    size=20 + (persen / max_persen) * 40,  # Ukuran minimal 20, maksimal 60
                    color=warna_jurusan[jurusan]
                )
                for jurusan, persen in hasil_rekomendasi.items()
            ]

            # Edge (hubungan antara kriteria yang dipilih dan jurusan yang direkomendasikan)
            edges = [
                Edge(source=kriteria, target=jurusan, color="#2c3e50")
                for kriteria, jurusan in relations_filtered if jurusan in hasil_rekomendasi
            ]

            # Konfigurasi Graph
            config = Config(
                width=750, 
                height=750,
                nodeHighlightBehavior=True,
                highlightColor="#fff",
                directed=True, 
                physics=True, 
                hierarchical=False
            )
            agraph(nodes=nodes, edges=edges, config=config)

        else:
            st.warning("⚠️ Tidak ada rekomendasi yang sesuai.")
    else:
        st.warning("⚠️ Silakan pilih minimal satu kriteria.")
