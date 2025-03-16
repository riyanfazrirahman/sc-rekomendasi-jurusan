import sqlite3
from collections import Counter

def get_recommendation(kriteria_user):
    
    # Koneksi ke Database SQLite
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    if not kriteria_user:
        return {} 

    placeholder = ", ".join(["?"] * len(kriteria_user))

    # Jika tidak ada input, return kosong
    query = f"SELECT id_kriteria FROM kriteria WHERE kode_kriteria IN ({placeholder})"
    cursor.execute(query, kriteria_user)
    id_kriteria_list = [row[0] for row in cursor.fetchall()]

    # Jika tidak ada yang cocok, return kosong
    if not id_kriteria_list:
        conn.close()
        return {} 

    # Cari jurusan berdasarkan id_kriteria
    placeholder = ", ".join(["?"] * len(id_kriteria_list))
    query = f"""
        SELECT jurusan.nama_jurusan 
        FROM aturan
        JOIN jurusan ON aturan.id_jurusan = jurusan.id_jurusan
        WHERE aturan.id_kriteria IN ({placeholder})
    """
    cursor.execute(query, id_kriteria_list)
    hasil = cursor.fetchall()

    # Menghitung Probabilitas Jurusan
    if hasil:
        jurusan_counts = Counter([item[0] for item in hasil])  # Hitung kemunculan jurusan
        total_rules_matched = sum(jurusan_counts.values())

        probabilitas = {jurusan: (count / total_rules_matched) * 100 
                        for jurusan, count in jurusan_counts.items()}
    else:
        probabilitas = {}
    conn.close()

    # Hasil Akhir: Rekomendasi Jurusan
    return probabilitas

