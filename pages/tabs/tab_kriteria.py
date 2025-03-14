import streamlit as st
from models.insert_default import table_kriteria
from models.kriteria_model import *

def show():
    # Tampilkan DataFrame Kriteria
    st.header("📌 Daftar Kriteria")
   
    df_kriteria = get_all_kriteria()
    st.dataframe(
        df_kriteria, 
        use_container_width=True, 
        hide_index=True
    )
  
    # Menambahkan kriteria baru
    row1_col1, row1_col2, row1_col3, row1_col4_b1 = st.columns(4)
    with row1_col1:
        row1_col1_a, row1_col1_b = st.columns(2) 
        with row1_col1_a:
            if st.button("📝 Default Kriteria", use_container_width=True):
                table_kriteria()
                st.rerun()  # Refresh 
        with row1_col1_b:
            if st.button("🗑️ Semua Kriteria", use_container_width=True):
                delete_all_kriteria()
                st.rerun()  # Refresh
    
    st.markdown("---")

    row2_col1, row2_col2 = st.columns(2, gap="large")
    with row2_col1:
        # Menambahkan kriteria baru
        st.header("🏷️ Tambah Kriteria")

        row2_col1_a, row2_col1_b = st.columns(2)
        with row2_col1_a:
            kode_kriteria_baru = st.text_input("Kode Kriteria")
        with row2_col1_b:
            nama_kriteria_baru = st.text_input("Nama Kriteria")
        
        row2_col1_row1_col1, row2_col1_row1_col2, row2_col1_row1_col3, row2_col1_row1_col4 = st.columns(4)
        with row2_col1_row1_col1:
            if st.button("Tambahkan Kriteria",  use_container_width=True):
                if kode_kriteria_baru and nama_kriteria_baru:
                    pesan = add_kriteria(kode_kriteria_baru, nama_kriteria_baru)
                    st.success(pesan)
                    st.rerun()  # Refresh

    
    with row2_col2:
        # Menghapus kriteria 
        st.header("🗑️ Hapus Kriteria")

        kriteria_list = get_kode_kriteria()
        kriteria_selected = st.multiselect("Pilih kode kriteria yang akan hapus:", kriteria_list)

        row2_col2_row2_col1, row2_col2_row2_col2, row2_col2_row2_col3, row2_col2_row2_col4 = st.columns(4)
        with row2_col2_row2_col1:
            if st.button("Hapus Kriteria",  use_container_width=True):
                if kriteria_selected:
                    for kode_kriteria in kriteria_selected:
                        delete_kriteria_by_kode(kode_kriteria)
                    st.success("✅ Kriteria berhasil dihapus!")
                    st.rerun()  # Refresh 

           