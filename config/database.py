import sqlite3

def init_db():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Tabel Jurusan
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jurusan (
        id_jurusan INTEGER PRIMARY KEY AUTOINCREMENT,
        kode_jurusan TEXT UNIQUE, 
        nama_jurusan TEXT 
    )
    """)

    # Tabel Kriteria
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kriteria (
        id_kriteria INTEGER PRIMARY KEY AUTOINCREMENT,
        kode_kriteria TEXT UNIQUE, 
        nama_kriteria TEXT 
    )
    """)

    # Tabel Aturan rekomendasi (relasi kriteria → jurusan)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS aturan (
        id_aturan INTEGER PRIMARY KEY AUTOINCREMENT,
        id_kriteria INTEGER,
        id_jurusan INTEGER,
        FOREIGN KEY (id_kriteria) REFERENCES kriteria(id_kriteria),
        FOREIGN KEY (id_jurusan) REFERENCES jurusan(id_jurusan)
    )
    """)

    # Tabel pengguna (admin/user)
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
