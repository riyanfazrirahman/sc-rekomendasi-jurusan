import streamlit as st
import pages.tabs.tab_users as tab_users
from pages.component.chart_line import get_history_stats

# Halaman Dashboard
st.title("📊 Tabel Pengguna")

# Tab 
tab1, tab2 = st.tabs(["📌 Data Pengguna", "📊 Statistik"])

with tab1:
    tab_users.show()

with tab2:
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