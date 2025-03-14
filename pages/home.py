import streamlit as st
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
        else:
            st.warning("⚠️ Tidak ada rekomendasi yang sesuai.")
    else:
        st.warning("⚠️ Silakan pilih minimal satu kriteria.")
