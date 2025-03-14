import streamlit as st
from models.insert_default import table_jurusan
from models.jurusan_model import *

def show():
    # Tampilkan DataFrame Jurusan
    st.header("📌 Daftar Jurusan")

    df_jurusan = get_all_jurusan()
    st.dataframe(
        df_jurusan, 
        use_container_width=True, 
        hide_index=True
    )
    
    # Menambahkan jurusan baru
    row1_col1, row1_col2, row1_col3, row1_col4_b1 = st.columns(4)
    with row1_col1:
        row1_col1_a, row1_col1_b = st.columns(2) 
        with row1_col1_a:
            if st.button("📝 Default Jurusan", use_container_width=True):
                table_jurusan()
                st.rerun()  # Refresh 
        with row1_col1_b:
            if st.button("🗑️ Semua Jurusan", use_container_width=True):
                delete_all_jurusan()
                st.rerun()  # Refresh
    
    st.markdown("---")

    row2_col1, row2_col2 = st.columns(2, gap="large")
    with row2_col1:
        # Menambahkan jurusan baru
        st.header("🏷️ Tambah Jurusan")

        row2_col1_a, row2_col1_b = st.columns(2)
        with row2_col1_a:
            kode_jurusan_baru = st.text_input("Kode Jurusan")
        with row2_col1_b:
            nama_jurusan_baru = st.text_input("Nama Jurusan")
        
        row2_col1_row1_col1, row2_col1_row1_col2, row2_col1_row1_col3, row2_col1_row1_col4 = st.columns(4)
        with row2_col1_row1_col1:
            if st.button("Tambahkan Jurusan",  use_container_width=True):
                if kode_jurusan_baru and nama_jurusan_baru:
                    pesan = add_jurusan(kode_jurusan_baru, nama_jurusan_baru)
                    st.success(pesan)
                    st.rerun()  # Refresh

    
    with row2_col2:
        # Menghapus jurusan 
        st.header("🗑️ Hapus jurusan")

        jurusan_list = get_kode_jurusan()
        jurusan_selected = st.multiselect("Pilih kode jurusan yang akan hapus:", jurusan_list)

        row2_col2_row2_col1, row2_col2_row2_col2, row2_col2_row2_col3, row2_col2_row2_col4 = st.columns(4)
        with row2_col2_row2_col1:
            if st.button("Hapus Jurusan",  use_container_width=True):
                if jurusan_selected:
                    for kode_jurusan in jurusan_selected:
                        delete_jurusan_by_kode(kode_jurusan)
                    st.success("✅ Jurusan berhasil dihapus!")
                    st.rerun()  # Refresh 