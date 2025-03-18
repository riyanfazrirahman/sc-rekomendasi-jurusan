import streamlit as st
from models.rekomendasi_model import get_summary_counts

# Halaman Home
st.title("🎓 Sistem Rekomendasi Jurusan Kuliah STMIK Palangka Raya")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
        <div style='margin: 2rem 0 2rem 0;text-align: center;'>
            <img src='https://raw.githubusercontent.com/riyanfazrirahman/sc-rekomendasi-jurusan/main/assets/img/logo_stmikplk.png' width='250'>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        ## 📌 Tentang Sistem
                
        Sistem ini menggunakan metode **Forward Chaining** untuk memberikan rekomendasi jurusan
        berdasarkan kriteria yang telah ditentukan. Pengguna akan diberikan beberapa pertanyaan
        terkait minat dan kemampuan, kemudian sistem akan menganalisis jawaban untuk
        menentukan jurusan yang paling sesuai.
        
        **Silakan mulai dengan menjawab pertanyaan untuk mendapatkan rekomendasi terbaik!**
        """,
        unsafe_allow_html=True
    )

    if st.button("Mulai Rekomendasi 🎯"):
        st.switch_page("pages/form_rekomendasi.py")


st.markdown("---")

col3, col4, col5 = st.columns(3)
card_style = """
    <style>
        .card {
            background-color: rgba(255, 255, 255, 0.1);
            color: inherit;
            padding: 20px;
            margin: 5px;
            border-radius: 10px;
            text-align: left;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        @media (prefers-color-scheme: dark) {
            .card {
                background-color: rgba(50, 50, 50, 0.5);
                color: white;
            }
        }
    </style>
"""

st.markdown(card_style, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class='card'>
            <h4>🔍 Fitur Utama</h4>
            <ul>
                <li>Rekomendasi jurusan berdasarkan preferensi pengguna</li>
                <li>Analisis berbasis aturan menggunakan <b>Forward Chaining</b></li>
                <li>Antarmuka yang mudah digunakan</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class='card'>
            <h4>🎓 Jurusan</h4>
            <ul>
                <li>Teknik Informatika</li>
                <li>Sistem Informasi</li>
                <li>Manajemen Informatika</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col5:
    counts = get_summary_counts()
    st.markdown(f"""
        <div class='card'>
            <h4>📊 Jumlah Kriteria</h4>
            <ul>
                <li>{counts["Kriteria"]} Kriteria </li>
                <li>{counts["Pertanyaan"]} Pertanyaan Penentuan</li>
                <li>{counts["Kategori"]} Kategori Pertanyan</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <h4>👨‍💻 Tim Pengembang</h4>
        <p style='margin:0'>Riyan Fazri Rahman | Raf'ad Amin Jayadi | Alif Rahmatullah Lesmana</p>
        <p style='margin-bottom: 2rem'>Nazia Fitra Aini | Oga Luisca Mika Sangga</p>
        <a href="https://www.stmikplk.ac.id/" style="text-decoration:none; color: #FF3333;">STMIK Palangka Raya - 2025</a>
    </div>
    """, unsafe_allow_html=True)
