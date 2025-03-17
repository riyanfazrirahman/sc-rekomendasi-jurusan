import sqlite3
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

def get_summary_counts():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    tables = {
        "Jurusan": "jurusan",
        "Kriteria": "kriteria",
        "Pertanyaan": "pertanyaan",
        "User": "users",
        "Histori": "riwayat_jawaban"
    }
    
    counts = {}
    for key, table in tables.items():
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        counts[key] = cursor.fetchone()[0]
    
    conn.close()
    return counts

# Halaman Dashboard
st.title("📊 Dashboard Statistik")

counts = get_summary_counts()

col1, col2, col3 = st.columns(3, gap="large")

def create_stat_card(title, value, bg_color, icon):
    st.markdown(f"""
        <div style='margin-bottom:20px; background-color:{bg_color}; padding:20px; border-radius:10px; color:#000; text-align:center;'>
            <h3 style='margin-bottom:5px;'>{icon} {title}</h3>
            <h2 style='margin:0;'>{value}</h2>
        </div>
    """, unsafe_allow_html=True)

with col1:
    create_stat_card("Jurusan", counts["Jurusan"], "#E3F2FD", "🎓")
    create_stat_card("User", counts["User"], "#E8F5E9", "👥")

with col2:
    create_stat_card("Kriteria", counts["Kriteria"], "#FFF3E0", "📌")
    create_stat_card("Histori", counts["Histori"], "#FCE4EC", "📜")

with col3:
    create_stat_card("Pertanyaan", counts["Pertanyaan"], "#E1F5FE", "❓")

# Styling metric cards
style_metric_cards(border_left_color="#42A5F5")