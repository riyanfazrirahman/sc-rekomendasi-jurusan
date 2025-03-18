import streamlit as st
from models.rekomendasi_model import get_summary_counts
from pages.component.chart_line import get_history_stats

# Halaman Dashboard
st.title("📊 Dashboard")

st.markdown("---")

counts = get_summary_counts()

cards = [
    ("Jurusan", counts["Jurusan"], "#E3F2FD", "🎓"),
    ("Kriteria", counts["Kriteria"], "#FFF3E0", "📌"),
    ("Pertanyaan", counts["Pertanyaan"], "#E1F5FE", "❓"),
    ("Kategori", counts["Kategori"], "#FFE6FF", "🏷️"),
    ("User", counts["User"], "#E8F5E9", "👥"),
    ("Histori", counts["Histori"], "#FCE4EC", "📜"),
]

col1, col2, col3 = st.columns(3)

def create_stat_card(title, value, bg_color, icon):
    st.markdown(f"""
        <div style='margin-bottom:20px; background-color:{bg_color}; padding: 15px; border-radius:10px; color:#000; text-align:center;'>
            <h3 style='border-bottom:1px solid black'>{icon} {title}</h3>
            <h2 style='margin: 20px 0;'>{value}</h2>
        </div>
    """, unsafe_allow_html=True)

# Tentukan jumlah kolom yang diinginkan
num_cols = 3  # Ubah sesuai kebutuhan (misal: 2, 3, 4, dst.)

# Buat kolom dinamis berdasarkan jumlah yang diatur
cols = st.columns(num_cols)

# Looping untuk mengisi kolom dengan data
for idx, (title, value, bg_color, icon) in enumerate(cards):
    with cols[idx % num_cols]:  # Distribusi card ke dalam kolom
        create_stat_card(title, value, bg_color, icon)


# Tampilkan Chart
st.header("📊 Statistik History Rekomendasi")

# Pilihan tampilan (Harian, Bulanan, Tahunan)
filter_option = st.selectbox("Tampilkan berdasarkan:", ["Harian", "Bulanan", "Tahunan"])

# Mapping pilihan ke fungsi
group_by = "day" if filter_option == "Harian" else "month" if filter_option == "Bulanan" else "year"
df_history = get_history_stats(group_by)

# Tampilkan chart
if not df_history.empty:
    st.line_chart(df_history, x="Periode", y="Jumlah History", use_container_width=True)
else:
    st.warning("Belum ada data history rekomendasi.")
    st.warning("Belum ada data riwayat pengguna.")
