import sqlite3
import pandas as pd

# Mengambil daftar pertanyaan berdasarkan kategori
def get_all_pertanyaan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_pertanyaan, kode_pertanyaan, pertanyaan, jenis_pertanyaan 
        FROM pertanyaan 
        WHERE jenis_pertanyaan IN ('single', 'multiple')
    """)
    
    pertanyaan_list = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(pertanyaan_list, columns=["ID", "Kode Pertanyaan", "Pertanyaan", "Jenis Pertanyaan"])
    return df 

def get_pertanyaan_has_kriteria():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.kode_pertanyaan, p.pertanyaan, k.kode_kriteria, k.nama_kriteria
        FROM pertanyaan_has_kriteria khp
        JOIN pertanyaan p ON khp.id_pertanyaan = p.id_pertanyaan
        JOIN kriteria k ON khp.id_kriteria = k.id_kriteria
    """)

    data = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(data,  columns=[ "Kode Pertanyaan", "Pertanyaaan", "Kode Kriteria", "Kriteria"])
    return df

# Mengambil data kategori, pertanyaan, dan kriterianya dari database
def format_pertanyaan_kriteria():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT k.kode_kategori, k.nama_kategori, p.kode_pertanyaan, p.pertanyaan, p.jenis_pertanyaan, kr.kode_kriteria, kr.nama_kriteria
        FROM kategori_has_pertanyaan khp
        JOIN kategori k ON khp.id_kategori = k.id_kategori
        JOIN pertanyaan p ON khp.id_pertanyaan = p.id_pertanyaan
        LEFT JOIN pertanyaan_has_kriteria phk ON p.id_pertanyaan = phk.id_pertanyaan
        LEFT JOIN kriteria kr ON phk.id_kriteria = kr.id_kriteria
        ORDER BY k.id_kategori, p.id_pertanyaan
    """)

    data = cursor.fetchall()
    conn.close()

    return data

