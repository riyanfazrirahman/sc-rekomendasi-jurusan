import streamlit as st
from models.auth_model import login_user, register_user

# Inisialisasi session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.user_id = None  
    st.session_state.username = None

# Layout form login/register
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    with st.container(border=True):
        st.title("🔑 Selamat Datang!")

        # Tabs Login & Register
        tab_login, tab_register = st.tabs(["🔓 Login", "📝 Register"])
        st.markdown("Pilih tab di atas untuk **Login** atau **Register**.")

        with tab_login:
            st.subheader("Masukkan username dan password untuk login.")
            username = st.text_input("👤 Username", placeholder="Masukkan username")
            password = st.text_input("🔑 Password", type="password", placeholder="Masukkan password")
            login_button = st.button("🚀 Login", use_container_width=True)

        with tab_register:
            st.subheader("Buat akun baru untuk menggunakan sistem.")
            new_username = st.text_input("👤 Username Baru", placeholder="Masukkan username baru")
            new_password = st.text_input("🔑 Password Baru", type="password", placeholder="Masukkan password")
            confirm_password = st.text_input("🔁 Konfirmasi Password", type="password", placeholder="Masukkan kembali password")
            register_button = st.button("📝 Register", use_container_width=True)

    # Proses login manual
    if login_button:
        user_id, role = login_user(username, password)  # Ambil user_id juga

        if role:
            st.session_state.logged_in = True
            st.session_state.role = role
            st.session_state.username = username
            st.session_state.user_id = user_id  

            st.toast(f"✅ Login berhasil sebagai **{role.capitalize()}**!", icon="✅")
            st.balloons()
            st.rerun()
        else:
            st.error("❌ Username atau password salah! Coba lagi.")

    # Proses register
    if register_button:
        if new_password != confirm_password:
            st.error("❌ Password tidak cocok! Coba lagi.")
        elif not new_username or not new_password:
            st.error("⚠️ Harap isi semua kolom!")
        else:
            success = register_user(new_username, new_password)
            if success:
                st.success("🎉 Registrasi berhasil! Silakan login.")
            else:
                st.error("⚠️ Username sudah digunakan. Gunakan yang lain.")
