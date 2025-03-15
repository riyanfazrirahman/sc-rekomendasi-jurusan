import sqlite3
import pandas as pd

# Mengambil daftar kategori
def get_all_kategori():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_kategori, kode_kategori, nama_kategori FROM kategori")
    kategori_list = cursor.fetchall()
    conn.close()

    df = pd.DataFrame(kategori_list, columns=["ID", "Kode Kategori", "Kategori"])
    return df 

def get_kategori_has_pertanyaan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT k.kode_kategori, k.nama_kategori, p.kode_pertanyaan, p.pertanyaan
        FROM kategori_has_pertanyaan khp
        JOIN kategori k ON khp.id_kategori = k.id_kategori
        JOIN pertanyaan p ON khp.id_pertanyaan = p.id_pertanyaan
    """)

    data = cursor.fetchall()
    conn.close()

    df = pd.DataFrame(data, columns=["Kode Kategori", "Nama Kategori", "Kode Pertanyaan", "Pertanyaaan"])
    return df

