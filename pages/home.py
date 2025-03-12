import streamlit as st
import sqlite3
from collections import Counter

def insert_default_rules():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    aturan_awal = [
        ("Matematika", "Teknik Informatika"),
        ("Pemrograman", "Teknik Informatika"),
        ("Sistem Komputer", "Teknik Informatika"),
        ("Biologi", "Kedokteran"),
        ("Kimia", "Kedokteran"),
        ("Anatomi", "Kedokteran"),
        ("Bisnis", "Manajemen"),
        ("Keuangan", "Manajemen"),
        ("Pemasaran", "Manajemen"),
    ]
    
    cursor.execute("SELECT COUNT(*) FROM aturan")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO aturan (minat, jurusan) VALUES (?, ?)", aturan_awal)
        conn.commit()
    
    conn.close()

def get_recommendation(minat_user):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT jurusan FROM aturan WHERE minat IN ({})".format(
        ", ".join(["?"] * len(minat_user))), minat_user)
    hasil = cursor.fetchall()
    conn.close()
    
    if hasil:
        jurusan_counts = Counter([item[0] for item in hasil])
        total_rules_matched = sum(jurusan_counts.values())
        probabilitas = {jurusan: (count / total_rules_matched) * 100 for jurusan, count in jurusan_counts.items()}
        return probabilitas
    else:
        return {}

def get_all_minat():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT minat FROM aturan")
    hasil = [row[0] for row in cursor.fetchall()]
    conn.close()
    return hasil


# Inisialisasi database dan aturan
# insert_default_rules()

# Input minat dari user
minat_list = get_all_minat()
st.title("🎓 Sistem Rekomendasi Jurusan dengan Probabilitas")
st.markdown("---")
st.subheader("📌 Pilih Minat Kamu")
minat_user = st.multiselect("Pilih minat yang sesuai dengan kamu:", minat_list)

# Tombol rekomendasi
tombol_rekomendasi = st.button("🔍 Dapatkan Rekomendasi")
if tombol_rekomendasi:
    if minat_user:
        hasil_rekomendasi = get_recommendation(minat_user)
        if hasil_rekomendasi:
            st.markdown("### 📊 Hasil Rekomendasi")
            for jurusan, persen in sorted(hasil_rekomendasi.items(), key=lambda x: x[1], reverse=True):
                st.progress(persen / 100)
                st.write(f"**{jurusan}: {persen:.2f}%**")
        else:
            st.warning("⚠️ Tidak ada rekomendasi yang sesuai.")
    else:
        st.warning("⚠️ Silakan pilih minimal satu minat.")