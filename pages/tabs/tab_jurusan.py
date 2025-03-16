import streamlit as st
from models.jurusan_model import *
from models.insert_default import table_jurusan
from pages.component.utils import buat_kode_terbaru

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
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("📝 Default Jurusan", use_container_width=True):
            table_jurusan()
            st.rerun()  # Refresh 
    with col2:
        if st.button("🗑️ Semua Jurusan", use_container_width=True):
            pesan = delete_all_jurusan()
            if "✅" in pesan:
                st.success(pesan)
                st.rerun()  # Refresh
            else:
                st.warning(pesan)  # Tampilkan pesan kesalahan
    
    st.markdown("---")

    left, right = st.columns(2, gap="large")
    with left:
        # Menambahkan jurusan baru
        st.header("🏷️ Tambah Jurusan")
        nama_jurusan_baru = st.text_input("Nama Jurusan")

        left_kode, left_btn1, left_s = st.columns(3)
        with left_kode:
            kode_terakhir = ", ".join(df_jurusan["Kode Jurusan"].iloc[-2:].tolist()) if df_jurusan is not None and not df_jurusan.empty else "-"
            default_kode_baru = buat_kode_terbaru(df_jurusan, kolom="Kode Jurusan")
            
            kode_jurusan_baru = st.text_input(f"Kode jurusan: `{kode_terakhir}, ...`", default_kode_baru)
        with left_btn1:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
            if st.button("Tambahkan Jurusan",  use_container_width=True):
                if kode_jurusan_baru and nama_jurusan_baru:
                    pesan = add_jurusan(kode_jurusan_baru, nama_jurusan_baru)
                    if "✅" in pesan:
                        st.success(pesan)
                        st.rerun()  # Refresh
                    else:
                        st.warning(pesan)  # Tampilkan pesan kesalahan

    
    with right:
        # Menghapus jurusan 
        st.header("🗑️ Hapus jurusan")

        jurusan_list = get_kode_jurusan()
        jurusan_selected = st.multiselect("Pilih kode jurusan yang akan hapus:", jurusan_list)

        right_btn1, right_btn2, = st.columns([1, 2])
        with right_btn1:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
            if st.button("Hapus Jurusan",  use_container_width=True):
                if jurusan_selected:
                    for kode_jurusan in jurusan_selected:
                        delete_jurusan_by_kode(kode_jurusan)
                    st.success("✅ Jurusan berhasil dihapus!")
                    st.rerun()  # Refresh 
                else:
                    st.warning(pesan)  # Tampilkan pesan kesalahan