import streamlit as st
import sqlite3

def login_user(username, password):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()
    return user[0] if user else None

st.title("🔑 Login Sistem")
st.markdown("---")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
login_button = st.button("Login")

if login_button:
    role = login_user(username, password)

    if role:
        st.session_state.logged_in = True
        st.session_state.role = role
        st.session_state.username = username
        st.success(f"Login berhasil sebagai {role.capitalize()}!")
        st.rerun()
    else:
        st.error("Username atau password salah!")

