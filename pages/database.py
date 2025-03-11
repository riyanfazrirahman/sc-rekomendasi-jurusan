import streamlit as st
import sqlite3
import pandas as pd

# Tombol kembali ke halaman utama
st.page_link("app.py", label="Halaman Utama", icon="🏠")
st.title("📊 Database")

# Fungsi untuk mengambil data dari database
def lihat_database():
    conn = sqlite3.connect("rekomendasi.db")
    df = pd.read_sql_query("SELECT * FROM aturan", conn)
    conn.close()
    return df

st.dataframe(lihat_database())  # Menampilkan tabel di Streamlit


