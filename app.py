import streamlit as st
from config.database import init_db  

# Inisialisasi database dan aturan
init_db()

# Inisialisasi session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

# Halaman logout
def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = None
    st.session_state.user_id = None  
    st.rerun()

# Tampilan utama
st.set_page_config(
    page_title="Rekomendasi Jurusan",
    page_icon="🎓",
    layout="wide",
)

home_page = st.Page("pages/home.py", title="Home", icon="🏠", default=True)
home_page_admin = st.Page("pages/home.py", title="Home", icon="🏠")
dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon="📊", default=True)
tabel_rekomendasi = st.Page("pages/tabel_rekomendasi.py", title="Tabel Rekomendasi", icon="📂")
tabel_pertanyaan = st.Page("pages/tabel_pertanyaan.py", title="Tabel Pertanyaan", icon="📂")
history = st.Page("pages/history.py", title="Riwayat", icon="📜")
tree = st.Page("pages/tree.py", title="Tree", icon="🌳")
setting = st.Page("pages/setting.py", title="Setting", icon="⚙️")

login_page = st.Page("pages/auth.py", title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

if st.session_state.logged_in:
    if st.session_state.role == "admin":
        pg = st.navigation(
            {
                "Account": [
                    logout_page,
                    setting,
                ],
                "Menu": [
                    home_page_admin, 
                    dashboard,
                ],
                "Data": [
                    tabel_rekomendasi,
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
                    home_page,
                    history
                ],
            }
        )
else:
    pg = st.navigation([
        login_page, 
        home_page, 
        tabel_rekomendasi,
        tabel_pertanyaan,
    ])

pg.run()
