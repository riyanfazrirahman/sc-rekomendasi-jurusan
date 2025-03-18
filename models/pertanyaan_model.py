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
        SELECT id_pertanyaan_kriteria, p.kode_pertanyaan, p.pertanyaan, k.kode_kriteria, k.nama_kriteria
        FROM pertanyaan_has_kriteria khp
        JOIN pertanyaan p ON khp.id_pertanyaan = p.id_pertanyaan
        JOIN kriteria k ON khp.id_kriteria = k.id_kriteria
    """)

    data = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(data,  columns=["ID", "Kode Pertanyaan", "Pertanyaaan", "Kode Kriteria", "Kriteria"])
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

def get_kode_pertanyaan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT kode_pertanyaan FROM pertanyaan ")
    kode_pertanyaan = [row[0] for row in cursor.fetchall()]
    conn.close()
    return kode_pertanyaan

# Tamabah data pertanyaan
def add_pertanyaan(kode_pertanyaan_baru, pertanyaan_baru, jenis_pertanyaan_selected):
    if not jenis_pertanyaan_selected:
        return "⚠️ Jenis pertanyaan harus dipilih."
    
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    # Cek apakah pertanyaan sudah ada
    cursor.execute("SELECT COUNT(*) FROM pertanyaan WHERE kode_pertanyaan = ? OR pertanyaan = ?", 
               (kode_pertanyaan_baru, pertanyaan_baru))
    if cursor.fetchone()[0] > 0:
        conn.close()
        return "⚠️ Pertanyaan sudah ada di database."
    
    # Insert ke tabel pertanyaan
    cursor.execute("INSERT INTO pertanyaan (kode_pertanyaan, pertanyaan, jenis_pertanyaan) VALUES (?, ?, ?)",  
                 (kode_pertanyaan_baru, pertanyaan_baru, jenis_pertanyaan_selected))

    conn.commit()
    conn.close()
    return "✅ Pertanyaan berhasil ditambahkan."

def add_pertanyaan_kriteria(pertanyaan, kriteria_list):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    # Dapatkan id_pertanyaan dari database
    cursor.execute("SELECT id_pertanyaan FROM pertanyaan WHERE kode_pertanyaan = ?", (pertanyaan,))
    id_pertanyaan = cursor.fetchone()

    if not id_pertanyaan:
        conn.close()
        return "⚠️ Pertanyaan tidak ditemukan!"
    
    id_pertanyaan = id_pertanyaan[0]  # Ambil nilai ID dari tuple

    # Simpan relasi pertanyaan-kriteria satu per satu
    for kriteria in kriteria_list:
        cursor.execute("SELECT id_kriteria FROM kriteria WHERE kode_kriteria = ?", (kriteria,))
        id_kriteria = cursor.fetchone()

        if id_kriteria:
            id_kriteria = id_kriteria[0]
            cursor.execute("INSERT INTO pertanyaan_has_kriteria (id_pertanyaan, id_kriteria) VALUES (?, ?)", 
                           (id_pertanyaan, id_kriteria))
    
    conn.commit()
    conn.close()
    
    return "✅ Aturan pertanyaan-kriteria berhasil ditambahkan!"

# Edit jenis
def update_jenis_pertanyaan(id_pertanyaan, new_jenis):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE pertanyaan SET jenis_pertanyaan = ? WHERE id_pertanyaan = ?
    """, (new_jenis, id_pertanyaan))
    conn.commit()
    conn.close()

# Hapus semua pertanyaan
def delete_all_pertanyaan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kategori_has_pertanyaan")
    cursor.execute("DELETE FROM pertanyaan_has_kriteria")
    cursor.execute("DELETE FROM pertanyaan")  # Hapus semua pertanyaan
    conn.commit()
    conn.close()


# Hapus pertanyaan berdasarkan kode_pertanyaan
def delete_pertanyaan_by_kode(kode_pertanyaan):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Ambil ID pertanyaan dari kode_pertanyaan
    cursor.execute("SELECT id_pertanyaan FROM pertanyaan WHERE kode_pertanyaan = ?", (kode_pertanyaan,))
    hasil = cursor.fetchone()

    if hasil:
        id_pertanyaan = hasil[0]

        # Cek apakah ID ada di tabel terkait sebelum menghapus
        cursor.execute("SELECT COUNT(*) FROM kategori_has_pertanyaan WHERE id_pertanyaan = ?", (id_pertanyaan,))
        ada_di_kategori = cursor.fetchone()[0] > 0

        cursor.execute("SELECT COUNT(*) FROM pertanyaan_has_kriteria WHERE id_pertanyaan = ?", (id_pertanyaan,))
        ada_di_kriteria = cursor.fetchone()[0] > 0

        # Jika ada di tabel terkait, hapus dulu
        if ada_di_kategori:
            cursor.execute("DELETE FROM kategori_has_pertanyaan WHERE id_pertanyaan = ?", (id_pertanyaan,))
        
        if ada_di_kriteria:
            cursor.execute("DELETE FROM pertanyaan_has_kriteria WHERE id_pertanyaan = ?", (id_pertanyaan,))

        # Hapus pertanyaan di tabel utama
        cursor.execute("DELETE FROM pertanyaan WHERE id_pertanyaan = ?", (id_pertanyaan,))

        conn.commit()
        pesan = f"✅ Pertanyaan dengan kode '{kode_pertanyaan}' berhasil dihapus."
    else:
        pesan = f"⚠️ Pertanyaan dengan kode '{kode_pertanyaan}' tidak ditemukan."

    conn.close()
    return pesan

def delete_pertanyaan_kriteria_by_id(id_list):
    if not id_list:
        return "⚠️ Tidak ada ID yang dipilih."

    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Menghapus banyak data sekaligus dengan `IN`
    query = f"DELETE FROM pertanyaan_has_kriteria WHERE id_pertanyaan_kriteria IN ({','.join(['?'] * len(id_list))})"
    cursor.execute(query, id_list)

    conn.commit()
    conn.close()

    return "✅ Kategori berhasil dihapus!"