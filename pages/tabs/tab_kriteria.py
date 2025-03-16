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
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("📝 Default Kriteria", use_container_width=True):
            table_kriteria()
            st.rerun()  # Refresh 
    with col2:
        if st.button("🗑️ Semua Kriteria", use_container_width=True):
                delete_all_kriteria()
                st.rerun()  # Refresh
    
    st.markdown("---")

    left, right = st.columns(2, gap="large")
    with left:
        # Menambahkan kriteria baru
        st.header("🏷️ Tambah Kriteria")
        nama_kriteria_baru = st.text_input("Nama Kriteria")

        left_kode, left_btn1, left_s = st.columns(3)
        kode_terakhir = ""
        with left_kode:
            if df_kriteria is not None and not df_kriteria.empty:
                kode_terakhir = ", ".join(df_kriteria["Kode Kriteria"].iloc[-2:].tolist())  # Ambil 2 terakhir
            else:
                kode_terakhir = "-" 
            kode_kriteria_baru = st.text_input(f"Kode Kriteria: `{kode_terakhir}`")
        with left_btn1:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
            if st.button("Tambahkan Kriteria",  use_container_width=True):
                if kode_kriteria_baru and nama_kriteria_baru:
                    pesan = add_kriteria(kode_kriteria_baru, nama_kriteria_baru)
                    st.success(pesan)
                    st.rerun()  # Refresh

    
    with right:
        # Menghapus kriteria 
        st.header("🗑️ Hapus Kriteria")

        kriteria_list = get_kode_kriteria()
        kriteria_selected = st.multiselect("Pilih kode kriteria yang akan hapus:", kriteria_list)

        right_btn1, right_btn2, = st.columns([1, 2])
        with right_btn1:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
            if st.button("Hapus Kriteria",  use_container_width=True):
                if kriteria_selected:
                    for kode_kriteria in kriteria_selected:
                        delete_kriteria_by_kode(kode_kriteria)
                    st.success("✅ Kriteria berhasil dihapus!")
                    st.rerun()  # Refresh 

           