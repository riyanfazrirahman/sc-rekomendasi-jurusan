import streamlit as st
from models.pertanyaan_model import *
from models.insert_default import table_pertanyaan
from pages.component.utils import buat_kode_terbaru

def show():
    # Tampilkan DataFrame Pertanyaan
    st.header("📌 Daftar Pertanyaan")

    df_pertanyaan = get_all_pertanyaan()
    st.dataframe(
        df_pertanyaan, 
        use_container_width=True, 
        hide_index=True
    )
    
    # Menambahkan Pertanyaan baru
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("📝 Default Pertanyaan", use_container_width=True):
            table_pertanyaan()
            st.rerun()  # Refresh 
    
    with col2:
        if st.button("🗑️ Semua Pertanyaan", use_container_width=True):
            delete_all_pertanyaan()
            st.rerun()  # Refresh

    st.markdown("---")
  
    left, right = st.columns(2, gap="large")
    with left:
        # Menambahkan pertanyaan baru
        st.header("🏷️ Tambah Pertanyaan")
        pertanyaan_baru = st.text_input("Pertanyaan")

        left_kode, left_jenis, left_btn1 = st.columns(3)
        with left_kode:
            kode_terakhir = ", ".join(df_pertanyaan["Kode Pertanyaan"].iloc[-2:].tolist()) if df_pertanyaan is not None and not df_pertanyaan.empty else "-"
            default_kode_baru = buat_kode_terbaru(df_pertanyaan,  kolom="Kode Pertanyaan")
          
            kode_pertanyaan_baru = st.text_input(f"Kode Pertanyaan: `{kode_terakhir}, ...`", default_kode_baru)
        with left_jenis:
            jenis_pertanyaan_selected = st.radio("Pilih Jenis Pertanyaan:", ["single", "multiple"])
        with left_btn1:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
            if st.button("Tambahkan Pertanyaan", use_container_width=True):
                if kode_pertanyaan_baru and pertanyaan_baru and jenis_pertanyaan_selected:
                    pesan = add_pertanyaan(kode_pertanyaan_baru, pertanyaan_baru, jenis_pertanyaan_selected)
                    if "✅" in pesan:
                        st.success(pesan)
                        st.rerun()  # Refresh
                    else:
                        st.warning(pesan)  # Tampilkan pesan kesalahan
    
    with right:
        # Menghapus pertanyaan 
        st.header("🗑️ Hapus Pertanyaan")

        pertanyaan_list = get_kode_pertanyaan()
        pertanyaan_selected = st.multiselect("Pilih kode pertanyaan yang akan hapus:", pertanyaan_list)

        right_btn1, right_btn2, = st.columns([1, 2])
        with right_btn1:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
            if st.button("Hapus Pertanyaan",  use_container_width=True):
                if pertanyaan_selected:
                    for kode_pertanyaan in pertanyaan_selected:
                        delete_pertanyaan_by_kode(kode_pertanyaan)
                    st.success("✅ Pertanyaan berhasil dihapus!")
                    st.rerun()  # Refresh ""