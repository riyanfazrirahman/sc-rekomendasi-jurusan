import streamlit as st
from config.database import get_table_names, delete_db_table

st.markdown("🗑️ **Hapus Tabel Database**")

# Ambil daftar tabel dari database
tables = get_table_names()

# Buat dua kolom: dropdown (lebih lebar) dan tombol hapus (lebih kecil)
col_l, col_r = st.columns([6, 2])

with col_l:
    if tables:
        selected_table = st.selectbox("Pilih tabel yang akan dihapus:", tables, key="table_select")
    else:
        st.warning("⚠️ Tidak ada tabel dalam database.")

with col_r:
    if tables:  # Pastikan ada tabel sebelum menampilkan tombol
        st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
        if st.button("🗑️ Hapus", use_container_width=True, key="delete_btn"):
            delete_db_table(selected_table)
            st.success(f"✅ Tabel '{selected_table}' berhasil dihapus!")
            st.rerun()  # Reload UI agar daftar tabel diperbarui
