import streamlit as st
import graphviz
from models.kriteria_model import get_options_kriteria
from models.rekomendasi_model import *

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

            # Ambil hanya hubungan yang sesuai dengan jurusan yang direkomendasikan
            relations = get_relations_filtered(list(hasil_rekomendasi.keys()))

            # Buat visualisasi terpisah untuk setiap jurusan
            for jurusan in hasil_rekomendasi.keys():
                graph = graphviz.Digraph(engine="neato")
                graph.attr(rankdir="TB", size="6,4", nodesep="0.5", ranksep="0.5")

                st.markdown(f"### 🎓 {jurusan}")

                # Tambahkan hubungan hanya yang terkait dengan jurusan ini
                for parent, child in relations:
                    if child == jurusan:  # Tidak perlu filter di sini jika pakai SQL
                        graph.edge(parent, child)

                # Tampilkan diagram untuk jurusan ini
                st.graphviz_chart(graph, use_container_width=True)


        else:
            st.warning("⚠️ Tidak ada rekomendasi yang sesuai.")
    else:
        st.warning("⚠️ Silakan pilih minimal satu kriteria.")