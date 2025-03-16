import sqlite3
import pandas as pd

# Tamabah data kriteria
def add_kriteria(kode_kriteria_baru, nama_kriteria_baru):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    # Cek apakah kriteria sudah ada
    cursor.execute("SELECT COUNT(*) FROM kriteria WHERE kode_kriteria = ? OR nama_kriteria = ?", 
                   (kode_kriteria_baru, nama_kriteria_baru))
    if cursor.fetchone()[0] > 0:
        conn.close()
        return "⚠️ Kriteria sudah ada di database."
    
    # Insert ke tabel kriteria
    cursor.execute("INSERT INTO kriteria (kode_kriteria, nama_kriteria) VALUES (?, ?)",  
                 (kode_kriteria_baru, nama_kriteria_baru))

    conn.commit()
    conn.close()
    return "✅ Kriteria berhasil ditambahkan."

# Ambil semua kriteria dari database
def get_all_kriteria():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_kriteria, kode_kriteria, nama_kriteria FROM kriteria")  # Pilih kolom yang jelas
    hasil = cursor.fetchall()
    conn.close()
    # Konversi ke DataFrame
    df = pd.DataFrame(hasil, columns=["ID", "Kode Kriteria", "Nama Kriteria"])
    return df

# Ambil semua kriteria yang belum ada di aturan
def get_options_kriteria():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nama_kriteria FROM kriteria ")
    daftar_kriteria = [row[0] for row in cursor.fetchall()]
    conn.close()
    return daftar_kriteria

def get_kode_kriteria():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT kode_kriteria FROM kriteria ")
    kode_kriteria = [row[0] for row in cursor.fetchall()]
    conn.close()
    return kode_kriteria

# Hapus kriteria berdasarkan kode_kriteria
def delete_kriteria_by_kode(kode_kriteria):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    # Ambil ID kriteria dari kode_kriteria
    cursor.execute("SELECT id_kriteria FROM kriteria WHERE kode_kriteria = ?", (kode_kriteria,))
    hasil = cursor.fetchone()
    
    if hasil:
        id_kriteria = hasil[0]
        # Hapus aturan yang terkait
        cursor.execute("DELETE FROM aturan WHERE id_kriteria = ?", (id_kriteria,))
        # Hapus kriteria di tabel kriteria
        cursor.execute("DELETE FROM kriteria WHERE kode_kriteria = ?", (kode_kriteria,))
        conn.commit()
    conn.close()

# Hapus semua kriteria
def delete_all_kriteria():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM aturan")
    cursor.execute("DELETE FROM kriteria")  # Hapus semua kriteria
    conn.commit()
    conn.close()