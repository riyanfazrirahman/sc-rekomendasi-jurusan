import streamlit as st
from config.database import init_db  

# Inisialisasi database dan aturan
init_db()

# Inisialisasi session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None  # Bisa 'admin' atau 'user'

# Halaman logout
def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.rerun()

# Tampilan utama
st.set_page_config(
    page_title="Rekomendasi Jurusan",
    page_icon="🎓",
    layout="wide",
)

home_page = st.Page("pages/home.py", title="Home", icon=":material/home:", default=True)
dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/dashboard:")
tabel_pertanyaan = st.Page("pages/pertanyaan.py", title="Tabel Pertanyaan", icon=":material/dashboard:")
history = st.Page("pages/history.py", title="Riwayat", icon=":material/dashboard:")
tree = st.Page("pages/tree.py", title="Tree", icon=":material/dashboard:")

login_page = st.Page("pages/login.py", title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

if st.session_state.logged_in:
    if st.session_state.role == "admin":
        pg = st.navigation(
            {
                "Account": [logout_page],
                "Menu": [
                    home_page, 
                    dashboard,
                    tabel_pertanyaan,
                    history
                ],
            }
        )
    elif st.session_state.role == "user":
        pg = st.navigation(
            {
                "Account": [logout_page],
                "Menu": [
                    home_page
                ],
            }
        )
else:
    pg = st.navigation([
        login_page, 
        home_page, 
        history
        ])

pg.run()
