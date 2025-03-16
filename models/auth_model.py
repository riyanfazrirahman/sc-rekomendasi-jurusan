import sqlite3

DB_PATH = "rekomendasi.db"

def login_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id_user, role FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()
    return user if user else (None, None) 

def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users WHERE id_user=?", (user_id))
    result = cursor.fetchone()

    conn.close()
    return  result[0] if result else "Unknown"

def register_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                       (username, password, "user"))  # Default role = "user"
        conn.commit()
        conn.close()
        return True  # Registrasi berhasil
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Username sudah ada
