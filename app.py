import streamlit as st

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
login_page = st.Page("pages/login.py", title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
dashboard = st.Page("pages/database.py", title="Database", icon=":material/dashboard:")

if st.session_state.logged_in:
    if st.session_state.role == "admin":
        pg = st.navigation(
            {
                "Account": [logout_page],
                "Menu": [home_page, dashboard],
            }
        )
    elif st.session_state.role == "user":
        pg = st.navigation(
            {
                "Account": [logout_page],
                "Menu": [home_page],
            }
        )
else:
    pg = st.navigation([login_page, home_page])

pg.run()
