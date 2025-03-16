import streamlit as st
from models.kategori_model import *
from models.insert_default import table_kategori
from pages.component.utils import buat_kode_terbaru

def show():
    # Tampilkan DataFrame kategori
    st.header("📌 Daftar Kategori")

    df_kategori = get_all_kategori()
    st.dataframe(
        df_kategori, 
        use_container_width=True, 
        hide_index=True
    )
    
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("📝 Default Kategori", use_container_width=True):
            table_kategori()
            st.rerun()  # Refresh 
    with col2:
        if st.button("🗑️ Semua Kategori", use_container_width=True):
            pesan = delete_all_kategori()
            if "✅" in pesan:
                st.success(pesan)
                st.rerun()  # Refresh
            else:
                st.warning(pesan)  # Tampilkan pesan kesalahan

    st.markdown("---")
  
    left, right = st.columns(2, gap="large")
    with left:
        # Menambahkan pertanyaan baru
        st.header("🏷️ Tambah Kategori")
        kategori_baru = st.text_input("Kategori")

        left_kode, left_jenis, left_btn1 = st.columns(3)
        with left_kode:
            kode_terakhir = ", ".join(df_kategori["Kode Kategori"].iloc[-2:].tolist()) if df_kategori is not None and not df_kategori.empty else "-"
            default_kode_baru = buat_kode_terbaru(df_kategori,  kolom="Kode Kategori")
          
            kode_kategori_baru = st.text_input(f"Kode Kategori: `{kode_terakhir}, ...`", default_kode_baru)
        with left_btn1:
                st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
                if st.button("Tambahkan Kategori",  use_container_width=True):
                    if kode_kategori_baru and kategori_baru:
                        pesan = add_kategori(kode_kategori_baru, kategori_baru)
                        if "✅" in pesan:
                            st.success(pesan)
                            st.rerun()  # Refresh
                        else:
                            st.warning(pesan)  # Tampilkan pesan kesalahan  
            
    with right:
        # Menghapus kategori 
        st.header("🗑️ Hapus Kategori")

        kategori_list = get_kode_kategori()
        kategori_selected = st.multiselect("Pilih kode kategori yang akan hapus:", kategori_list)

        right_btn1, right_btn2, = st.columns([1, 2])
        with right_btn1:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
            if st.button("Hapus Kategori",  use_container_width=True):
                if kategori_selected:
                    for kode_kategori in kategori_selected:
                        delete_kategori_by_kode(kode_kategori)
                    st.success("✅ Kategori berhasil dihapus!")
                    st.rerun()  # Refresh 
