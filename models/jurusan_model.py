import sqlite3
import pandas as pd

# Tamabah data jurusan
def add_jurusan(kode_jurusan_baru, nama_jurusan_baru):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    # Cek apakah jurusan sudah ada
    cursor.execute("SELECT COUNT(*) FROM jurusan WHERE kode_jurusan = ? OR nama_jurusan = ?", 
                   (kode_jurusan_baru, nama_jurusan_baru))
    if cursor.fetchone()[0] > 0:
        conn.close()
        return "⚠️ Jurusan sudah ada di database."
    
    # Insert ke tabel jurusan
    cursor.execute("INSERT INTO jurusan (kode_jurusan, nama_jurusan) VALUES (?, ?)",  
                   (kode_jurusan_baru, nama_jurusan_baru))

    conn.commit()
    conn.close()
    return "✅ Jurusan berhasil ditambahkan."

# Ambil semua Jurusan dari database
def get_all_jurusan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_jurusan, kode_jurusan, nama_jurusan FROM jurusan")  # Pilih kolom yang jelas
    hasil = cursor.fetchall()
    conn.close()
    # Konversi ke DataFrame
    df = pd.DataFrame(hasil, columns=["ID", "Kode Jurusan", "Nama Jurusan"])
    return df

# Ambil semua jurusan dari database untuk dropdown
def get_options_jurusan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nama_jurusan FROM jurusan")
    daftar_jurusan = [row[0] for row in cursor.fetchall()]
    conn.close()
    return daftar_jurusan

def get_kode_jurusan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT kode_jurusan FROM jurusan ")
    kode_jurusan = [row[0] for row in cursor.fetchall()]
    conn.close()
    return kode_jurusan

# Simpan perubahan ke database
def update_jurusan(id_aturan, nama_jurusan_baru):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    # Cari id_jurusan berdasarkan nama jurusan baru
    cursor.execute("SELECT id_jurusan FROM jurusan WHERE nama_jurusan = ?", (nama_jurusan_baru,))
    id_jurusan_baru = cursor.fetchone()
    if id_jurusan_baru:
        id_jurusan_baru = id_jurusan_baru[0]
        cursor.execute("UPDATE aturan SET id_jurusan = ? WHERE id_aturan = ?", (id_jurusan_baru, id_aturan))
        conn.commit()
    conn.close()


# Hapus kriteria berdasarkan kode_jurusan
def delete_jurusan_by_kode(kode_jurusan):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    # Ambil ID kriteria dari kode_jurusan
    cursor.execute("SELECT id_jurusan FROM jurusan WHERE kode_jurusan = ?", (kode_jurusan,))
    hasil = cursor.fetchone()
    
    if hasil:
        id_jurusan = hasil[0]
        # Hapus aturan yang terkait
        cursor.execute("DELETE FROM aturan WHERE id_jurusan = ?", (id_jurusan,))
        # Hapus jurusan di tabel jurusan
        cursor.execute("DELETE FROM jurusan WHERE kode_jurusan = ?", (kode_jurusan,))
        conn.commit()
    conn.close()


# Hapus semua jurusan
def delete_all_jurusan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Hitung jumlah jurusan sebelum menghapus
    cursor.execute("SELECT COUNT(*) FROM jurusan")

    if jumlah_kategori > 0:
        jumlah_kategori = cursor.fetchone()[0]
        cursor.execute("DELETE FROM aturan")    # Hapus semua aturan
        cursor.execute("DELETE FROM jurusan")   # Hapus semua jurusan
        conn.commit()
        pesan = "✅ Semua kategori berhasil dihapus."
    else:
        pesan = "⚠️ Tidak ada kategori yang bisa dihapus."

    conn.close()
    return pesan  # Selalu mengembalikan pesan (string)


