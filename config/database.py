import sqlite3
from models.auth_model import hash_password

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
        FOREIGN KEY (id_kriteria) REFERENCES kriteria(id_kriteria) ON DELETE CASCADE, 
        FOREIGN KEY (id_jurusan) REFERENCES jurusan(id_jurusan) ON DELETE CASCADE
    )
    """)

    # Tabel pengguna (admin/user)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT CHECK(role IN ('admin', 'user'))
    )
    """)
    # delete_db_table("users")

    # Tabel Kategori 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kategori (
        id_kategori INTEGER PRIMARY KEY AUTOINCREMENT,
        kode_kategori TEXT NOT NULL,
        nama_kategori TEXT NOT NULL
    );
    """)

    # Tabel Pertanyaan 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pertanyaan (
        id_pertanyaan INTEGER PRIMARY KEY AUTOINCREMENT,
        kode_pertanyaan TEXT NOT NULL,
        pertanyaan TEXT NOT NULL,
        jenis_pertanyaan TEXT CHECK(jenis_pertanyaan IN ('single', 'multiple'))
    );
    """)

    # Tabel Kategori Pertanyaan  (relasi Kategori pertanyaan → ) 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kategori_has_pertanyaan (
        id_kategori_pertanyaan INTEGER PRIMARY KEY AUTOINCREMENT,
        id_kategori INTEGER,
        id_pertanyaan INTEGER,
        FOREIGN KEY (id_kategori) REFERENCES kategori(id_kategori) ON DELETE CASCADE,
        FOREIGN KEY (id_pertanyaan) REFERENCES pertanyaan(id_pertanyaan) ON DELETE CASCADE
    );
    """)

    # Tabel Pertanyaan Kriteria (relasi pertanyaan → kriteria)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pertanyaan_has_kriteria (
        id_pertanyaan_kriteria INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pertanyaan INTEGER,
        id_kriteria INTEGER,
        FOREIGN KEY (id_pertanyaan) REFERENCES pertanyaan(id) ON DELETE CASCADE,
        FOREIGN KEY (id_kriteria) REFERENCES kriteria(id) ON DELETE CASCADE
    );
    """)
    
    # Buat tabel untuk menyimpan jawaban user
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS riwayat_jawaban (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NULL,  -- Bisa NULL kalau user tidak login
        kode TEXT UNIQUE,
        jawaban TEXT,
        timestamp TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
    );
    """)
    
    # Tambahkan akun admin default jika belum ada
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        # hashed_admin_pass = "admin123"
        hashed_admin_pass = hash_password("admin123")
        cursor.execute("INSERT INTO users (username, password, role) VALUES ('admin', ?, 'admin')", (hashed_admin_pass,))

    conn.commit()
    conn.close()

def delete_db_table(nama_table):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Untuk Delet Tabel
    cursor.execute(f"""
    DROP TABLE {nama_table};
    """)

    conn.commit()
    conn.close()

def get_table_names():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_sequence;")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tables