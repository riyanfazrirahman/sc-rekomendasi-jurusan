import streamlit as st
from models.pertanyaan_model import (
    get_pertanyaan_has_kriteria, 
    get_kode_pertanyaan, 
    add_pertanyaan_kriteria, 
    delete_pertanyaan_kriteria_by_id
)
from models.kriteria_model import get_kode_kriteria
from models.insert_default import table_pertanyaan_has_kriteria

def show():
    # Tampilkan DataFrame Pertanyaan
    st.header("📌 Daftar Pertanyaan dan Kriterianya")

    df_pertanyaan_kriteria = get_pertanyaan_has_kriteria()

    st.dataframe(
        df_pertanyaan_kriteria,
        use_container_width=True,
        hide_index=True
    )

    col1, col2, col3 = st.columns([1.2, 0.8, 4])
    with col1:
        if st.button("📝 Default Pertanyaan Kriteria", use_container_width=True):
            table_pertanyaan_has_kriteria()
            st.rerun()  # Refresh

    st.markdown("---")

    col4, col5 = st.columns(2, gap="large")
    with col4:
        # Menambahkan aturan baru
        st.header("🏷️ Tambah Pertanyaan Kriteria")

        pertanyaan_list = get_kode_pertanyaan()
        kriteria_list = get_kode_kriteria() 

        col6, col7 = st.columns([1, 2])
        with col6:
            pertanyaan_selected = st.selectbox("Pilih kode pertanyaan:", pertanyaan_list) 

        with col7:
            kriteria_selected = st.multiselect("Pilih kode kriteria yang dikaitkan ke pertanyaan:", kriteria_list)
        
        col8, col9 = st.columns([1, 2])
        with col8:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)

            if st.button("Tambahkan", use_container_width=True):
                if pertanyaan_selected and kriteria_selected:
                    pesan = add_pertanyaan_kriteria(pertanyaan_selected, kriteria_selected)
                    
                    if "✅" in pesan:
                        st.success(pesan)
                        st.rerun()  # Refresh
                    else:
                        st.warning(pesan)  # Tampilkan pesan kesalahan
                else:
                    st.warning("Harap isi semua bidang sebelum menambahkan aturan.")

    with col5:
        # Menghapus kategori 
        st.header("🗑️ Hapus Pertanyaan Kriteria")

        id_list = df_pertanyaan_kriteria["ID"].tolist()
        id_selected = st.multiselect("Pilih ID yang akan hapus:", id_list)

        col10, col11, = st.columns([1, 2])
        with col10:
            st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)
            if st.button("Hapus", key="Hapus Pertanyaan Kriteria", use_container_width=True):
                if id_selected:
                    pesan = delete_pertanyaan_kriteria_by_id(id_selected)  # Kirimkan list, bukan integer
                    st.success(pesan)
                    st.rerun()  # Refresh 
                else:
                    st.warning("⚠️ Harap pilih setidaknya satu ID untuk dihapus.")

