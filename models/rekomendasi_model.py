import sqlite3
import pandas as pd
from collections import Counter

# Ambil semua hubungan kriteria → jurusan
def get_relations():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT kriteria.kode_kriteria, jurusan.kode_jurusan 
        FROM aturan
        JOIN kriteria ON aturan.id_kriteria = kriteria.id_kriteria
        JOIN jurusan ON aturan.id_jurusan = jurusan.id_jurusan
    """)
    hasil = cursor.fetchall()  # List pasangan (kriteria, jurusan)
    conn.close()
    return hasil

def get_relations_filtered(jurusan_list):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    # Buat format query dengan filter jurusan
    placeholders = ", ".join(["?" for _ in jurusan_list])
    query = f"""
        SELECT kriteria.kode_kriteria, jurusan.kode_jurusan 
        FROM aturan
        JOIN kriteria ON aturan.id_kriteria = kriteria.id_kriteria
        JOIN jurusan ON aturan.id_jurusan = jurusan.id_jurusan
        WHERE jurusan.nama_jurusan IN ({placeholders})
    """
    
    cursor.execute(query, jurusan_list)
    hasil = cursor.fetchall()  # List pasangan (kriteria, jurusan)
    
    conn.close()
    return hasil

# Rekomendasi jurusan berdasarkan kriteria yang dipilih pengguna
def get_recommendation(kriteria_user):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    if not kriteria_user:
        return {}  # Jika tidak ada input, return dictionary kosong

    # Dapatkan id_kriteria dari nama_kriteria dengan parameter binding
    placeholder = ", ".join(["?"] * len(kriteria_user))
    query = f"SELECT id_kriteria FROM kriteria WHERE nama_kriteria IN ({placeholder})"
    cursor.execute(query, kriteria_user)
    id_kriteria_list = [row[0] for row in cursor.fetchall()]

    if not id_kriteria_list:
        conn.close()
        return {}  # Jika tidak ada id_kriteria yang cocok, return kosong

    # Ambil daftar jurusan berdasarkan id_kriteria yang cocok, langsung `JOIN` dengan tabel jurusan
    placeholder = ", ".join(["?"] * len(id_kriteria_list))
    query = f"""
        SELECT jurusan.nama_jurusan 
        FROM aturan
        JOIN jurusan ON aturan.id_jurusan = jurusan.id_jurusan
        WHERE aturan.id_kriteria IN ({placeholder})
    """
    cursor.execute(query, id_kriteria_list)
    hasil = cursor.fetchall()

    if hasil:
        jurusan_counts = Counter([item[0] for item in hasil])  # Count berdasarkan nama jurusan
        total_rules_matched = sum(jurusan_counts.values())

        probabilitas = {jurusan: (count / total_rules_matched) * 100 
                        for jurusan, count in jurusan_counts.items()}
    else:
        probabilitas = {}

    conn.close()
    return probabilitas
