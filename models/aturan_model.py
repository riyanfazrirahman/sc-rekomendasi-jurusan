import sqlite3
import pandas as pd

# Ambil data aturan dalam bentuk DataFrame
def get_all_aturan():
    conn = sqlite3.connect("rekomendasi.db")
    df = pd.read_sql_query("""
        SELECT 
            aturan.id_aturan, 
            kriteria.kode_kriteria, 
            kriteria.nama_kriteria, 
            jurusan.kode_jurusan, 
            jurusan.nama_jurusan
        FROM aturan
        JOIN kriteria ON aturan.id_kriteria = kriteria.id_kriteria
        JOIN jurusan ON aturan.id_jurusan = jurusan.id_jurusan
    """, conn)
    conn.close()
    return df

def add_aturan(nama_kriteria, nama_jurusan):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    # Dapatkan id_kriteria baru
    cursor.execute("SELECT id_kriteria FROM kriteria WHERE nama_kriteria = ?", (nama_kriteria,))
    id_kriteria = cursor.fetchone()
    
    # Dapatkan id_jurusan baru
    cursor.execute("SELECT id_jurusan FROM jurusan WHERE nama_jurusan = ?", (nama_jurusan,))
    id_jurusan = cursor.fetchone()
    
    if id_kriteria and id_jurusan:
        id_kriteria = id_kriteria[0]
        id_jurusan = id_jurusan[0]
        
        cursor.execute("INSERT INTO aturan (id_kriteria, id_jurusan) VALUES (?, ?)", 
                       (id_kriteria, id_jurusan))
        conn.commit()
    
    conn.close()


# Simpan perubahan ke database
def update_aturan(id_aturan, nama_kriteria_baru, nama_jurusan_baru):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    # Dapatkan id_kriteria baru
    cursor.execute("SELECT id_kriteria FROM kriteria WHERE nama_kriteria = ?", (nama_kriteria_baru,))
    id_kriteria_baru = cursor.fetchone()
    
    # Dapatkan id_jurusan baru
    cursor.execute("SELECT id_jurusan FROM jurusan WHERE nama_jurusan = ?", (nama_jurusan_baru,))
    id_jurusan_baru = cursor.fetchone()
    
    if id_kriteria_baru and id_jurusan_baru:
        id_kriteria_baru = id_kriteria_baru[0]
        id_jurusan_baru = id_jurusan_baru[0]
        
        cursor.execute("UPDATE aturan SET id_kriteria = ?, id_jurusan = ? WHERE id_aturan = ?", 
                       (id_kriteria_baru, id_jurusan_baru, id_aturan))
        conn.commit()
    
    conn.close()

def delete_aturan(id_aturan):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM aturan WHERE id_aturan = ?", (id_aturan,))
    
    conn.commit()
    conn.close()

