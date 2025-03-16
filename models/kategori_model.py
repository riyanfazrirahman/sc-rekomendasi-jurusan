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

# Tamabah data kategori
def add_kategori(kode_kategori_baru, kategori_baru):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    # Cek apakah kategori sudah ada
    cursor.execute("SELECT COUNT(*) FROM kategori WHERE kode_kategori = ? OR nama_kategori = ?", 
                   (kode_kategori_baru, kategori_baru))
    if cursor.fetchone()[0] > 0:
        conn.close()
        return "⚠️ Kategori sudah ada di database."
    
    # Insert ke tabel kategori
    cursor.execute("INSERT INTO kategori (kode_kategori, nama_kategori) VALUES (?, ?)",  
                 (kode_kategori_baru, kategori_baru))

    conn.commit()
    conn.close()
    return "✅ Kategori berhasil ditambahkan."

def get_kode_kategori():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT kode_kategori FROM kategori ")
    kode_kategori = [row[0] for row in cursor.fetchall()]
    conn.close()
    return kode_kategori

# Hapus semua kategori
def delete_all_kategori():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Hitung jumlah kategori sebelum menghapus
    cursor.execute("SELECT COUNT(*) FROM kategori")
    jumlah_kategori = cursor.fetchone()[0]

    if jumlah_kategori > 0:
        # Hapus semua kategori
        cursor.execute("DELETE FROM kategori")
        conn.commit()
        pesan = "✅ Semua kategori berhasil dihapus."
    else:
        pesan = "⚠️ Tidak ada kategori yang bisa dihapus."

    conn.close()
    return pesan  # Selalu mengembalikan pesan (string)


# Hapus kategori berdasarkan kode_kategori
def delete_kategori_by_kode(kode_kategori):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Ambil ID kategori dari kode_kategori
    cursor.execute("SELECT id_kategori FROM kategori WHERE kode_kategori = ?", (kode_kategori,))
    hasil = cursor.fetchone()

    pesan = "⚠️ Terjadi kesalahan."  # Default pesan jika ada error

    if hasil:
        id_kategori = hasil[0]

        # Cek apakah ID ada di tabel terkait sebelum menghapus
        cursor.execute("SELECT COUNT(*) FROM kategori_has_pertanyaan WHERE id_kategori = ?", (id_kategori,))
        ada_di_kategori = cursor.fetchone()[0] > 0

        # Jika ada di tabel terkait, hapus dulu
        if ada_di_kategori:
            cursor.execute("DELETE FROM kategori_has_pertanyaan WHERE id_kategori = ?", (id_kategori,))

        # Hapus kategori di tabel utama
        cursor.execute("DELETE FROM kategori WHERE id_kategori = ?", (id_kategori,))

        conn.commit()
        pesan = f"✅ Kategori dengan kode '{kode_kategori}' berhasil dihapus."
    else:
        pesan = f"⚠️ Kategori dengan kode '{kode_kategori}' tidak ditemukan."

    conn.close()
    return pesan