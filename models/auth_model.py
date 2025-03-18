import sqlite3
import bcrypt
import pandas as pd

DB_PATH = "rekomendasi.db"

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()  # Simpan dalam format string

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())  # Convert ke bytes dulu

def login_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Ambil password hash dari database
    cursor.execute("SELECT id_user, password, role FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    conn.close()

    if user:
        user_id, stored_hashed_password, role = user  # Ambil data
        if verify_password(password, stored_hashed_password):  # Cocokkan password hash
            return user_id, role  # Login berhasil

    return None, None  # Login gagal

def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users WHERE id_user=?", (user_id))
    result = cursor.fetchone()

    conn.close()
    return  result[0] if result else "Unknown"

# Fungsi mengambil semua pengguna
def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id_user, username, role FROM users")
    users = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(users, columns=["ID", "Username", "Role"])
    return df

# Fungsi mengupdate role user
def update_user_roles(df_users):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    for index, row in df_users.iterrows():
        cursor.execute("UPDATE users SET role = ? WHERE id_user = ?", (row["Role"], row["ID"]))
    
    conn.commit()
    conn.close()


def register_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    set_hash_password = hash_password(password)  # Ubah bytes → string

    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                       (username, set_hash_password, "user"))  # Default role = "user"
        conn.commit()
        conn.close()
        return True  # Registrasi berhasil
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Username sudah ada
