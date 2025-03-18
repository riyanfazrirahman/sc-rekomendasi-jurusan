import streamlit as st
from config.database import init_db  

# Tampilan utama
st.set_page_config(
    page_title="Rekomendasi Jurusan",
    page_icon="🎓",
    layout="wide",
)

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

home_page = st.Page("pages/home.py", title="Home", icon="🏠", default=True)
home_page_admin = st.Page("pages/home.py", title="Home", icon="🏠")
form_rekomendasi = st.Page("pages/form_rekomendasi.py", title="Form Rekomendasi", icon="📝")
dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon="📊", default=True)
tabel_rekomendasi = st.Page("pages/tabel_rekomendasi.py", title="Tabel Rekomendasi", icon="📂")
tabel_pertanyaan = st.Page("pages/tabel_pertanyaan.py", title="Tabel Pertanyaan", icon="📂")
tabel_users = st.Page("pages/tabel_users.py", title="Tabel Pengguna", icon="📂")
history = st.Page("pages/history.py", title="Riwayat", icon="📜")
setting = st.Page("pages/setting.py", title="Setting", icon="⚙️")
login_page = st.Page("pages/auth.py", title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

if st.session_state.logged_in:
    username_display = f"Selamat Datang, 👤 {st.session_state.username}"
    if st.session_state.role == "admin":
        pg = st.navigation(
            {
                username_display: [
                    logout_page,
                    setting,
                ],
                "Menu": [
                    home_page_admin,
                    dashboard,
                    form_rekomendasi, 
                ],
                "Data": [
                    tabel_rekomendasi,
                    tabel_pertanyaan,
                    tabel_users,
                    history
                ],
            }
        )
    elif st.session_state.role == "user":
        pg = st.navigation(
            {
                username_display: [
                    logout_page
                ],
                "Menu": [
                    home_page,
                    form_rekomendasi,
                    history
                ],
            }
        )
else:
    pg = st.navigation([
        login_page,
        home_page, 
        form_rekomendasi,
        # tabel_users
        # tabel_rekomendasi,
        # tabel_pertanyaan,
        # history
        # setting, 
    ])
pg.run()
