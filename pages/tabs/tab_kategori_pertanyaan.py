import streamlit as st
from models.kategori_model import (
    get_kategori_has_pertanyaan, 
    get_kode_kategori, 
    add_kategori_pertanyaan,
    delete_kategori_pertanyaan_by_id
)
from models.pertanyaan_model import get_kode_pertanyaan
from models.insert_default import table_kategori_has_pertanyan

def show():
    # Tampilkan DataFrame Pertanyaan
    st.header("📌 Daftar Kategori dan Pertanyaannya")

    df_kategori_pertanyaan = get_kategori_has_pertanyaan()
    st.dataframe(
        df_kategori_pertanyaan, 
        use_container_width=True, 
        hide_index=True
    )
        
    col1, col2, col3 = st.columns([1.2, 0.8, 4])
    with col1:
        if st.button(f"📝 Default \nKategori Pertanyaan", use_container_width=True):
            table_kategori_has_pertanyan()
            st.rerun()  # Refresh 
            
    st.markdown("---")

    col4, col5 = st.columns(2, gap="large")
    with col4:
        # Menambahkan aturan baru
        st.header("🏷️ Tambah Kategori Pertanyaan")

        kategori_list = get_kode_kategori() 
        pertanyaan_list = get_kode_pertanyaan()

        col6, col7 = st.columns([1, 2])
        with col6:
            kategori_selected = st.selectbox("Pilih kode kategori", kategori_list)

        with col7:
            pertanyaan_selected = st.multiselect("Pilih kode pertanyaan yang akan di kategorikan:", pertanyaan_list) 
        
        col8, col9 = st.columns([1, 2])
        with col8:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)

            if st.button("Kategorikan", use_container_width=True):
                if pertanyaan_selected and kategori_selected:
                    pesan = add_kategori_pertanyaan(kategori_selected, pertanyaan_selected)
                    
                    if "✅" in pesan:
                        st.success(pesan)
                        st.rerun()  # Refresh
                    else:
                        st.warning(pesan)  # Tampilkan pesan kesalahan
                else:
                    st.warning("Harap isi semua bidang sebelum menambahkan aturan.")

    with col5:
        # Menghapus kategori 
        st.header("🗑️ Hapus kategori Pertanyaan")

        id_list = df_kategori_pertanyaan["ID"].tolist()
        id_selected = st.multiselect("Pilih ID yang akan hapus:", id_list)

        col10, col11, = st.columns([1, 2])
        with col10:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
            if st.button("Hapus", key="Hapus Kategori Pertanyaan",  use_container_width=True):
                if id_selected:
                    pesan = delete_kategori_pertanyaan_by_id(id_selected)  # Kirimkan list, bukan integer
                    st.success(pesan)
                    st.rerun()  # Refresh 
                else:
                    st.warning("⚠️ Harap pilih setidaknya satu ID untuk dihapus.")
