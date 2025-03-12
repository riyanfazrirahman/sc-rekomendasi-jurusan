import streamlit as st
import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Tabel aturan rekomendasi
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS aturan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        minat TEXT,
        jurusan TEXT
    )
    """)

    # Tabel pengguna
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT CHECK(role IN ('admin', 'user'))
    )
    """)

    # Tambahkan akun admin default jika belum ada
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin')")
    
    conn.commit()
    conn.close()

def add_rule(minat, jurusan):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO aturan (minat, jurusan) VALUES (?, ?)", (minat, jurusan))
    conn.commit()
    conn.close()

# Fungsi untuk mengambil data dari database
def lihat_database():
    conn = sqlite3.connect("rekomendasi.db")
    df = pd.read_sql_query("SELECT * FROM aturan", conn)
    conn.close()
    return df

# Fungsi update aturan di database
def update_aturan(id, minat, jurusan):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE aturan SET minat = ?, jurusan = ? WHERE id = ?", (minat, jurusan, id))
    conn.commit()
    conn.close()

# Menghapus aturan berdasarkan ID
def hapus_aturan(ids):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.executemany("DELETE FROM aturan WHERE id = ?", [(i,) for i in ids])
    conn.commit()
    conn.close()
    st.rerun()  # Refresh halaman setelah penghapusan

# Inisialisasi database
init_db()

# Halaman database
st.title("📊 Database")
st.markdown("---")

# Menambahkan aturan baru
st.sidebar.header("➕ Tambah Aturan Baru")
minat_baru = st.sidebar.text_input("Masukkan Minat")
jurusan_baru = st.sidebar.text_input("Masukkan Jurusan")
if st.sidebar.button("Tambahkan Aturan"):
    if minat_baru and jurusan_baru:
        add_rule(minat_baru, jurusan_baru)
        st.sidebar.success("✅ Aturan berhasil ditambahkan!")
        st.rerun()
    else:
        st.sidebar.error("⚠️ Mohon isi kedua bidang sebelum menambahkan aturan.")

# Ambil data
df = lihat_database()

if not df.empty:
    st.write("### 📌 Daftar Aturan Rekomendasi")

    # Tambahkan kolom No untuk index
    df.insert(0, "no", range(1, len(df) + 1))

    edited_df = st.data_editor(
        df,
        num_rows="dynamic",
        column_config={
            "id": None,  # Sembunyikan ID
            "no": st.column_config.Column("No.", width="small"), # Ganti nama kolom
            "minat": st.column_config.Column("Minat", width="large"), # Ganti nama kolom
            "jurusan": st.column_config.Column("Rekomendasi Jurusan", width="large"), # Ganti nama kolom
        },
        disabled=["id"],  # ID tidak bisa diedit
        hide_index=True,  # Sembunyikan index default Pandas
    )

    # Simpan perubahan jika ada edit
    if not edited_df.equals(df):
        conn = sqlite3.connect("rekomendasi.db")
        cursor = conn.cursor()
        
        # Hapus semua data lama
        cursor.execute("DELETE FROM aturan")
        
        # Tambahkan data baru dari edited_df
        for _, row in edited_df.iterrows():
            cursor.execute("INSERT INTO aturan (id, minat, jurusan) VALUES (?, ?, ?)", 
                        (row["id"], row["minat"], row["jurusan"]))
        
        conn.commit()
        conn.close()
        
        st.success("✅ Perubahan berhasil disimpan!")
        st.rerun()  # Refresh halaman
    
else:
    st.info("Belum ada aturan yang ditambahkan.")

