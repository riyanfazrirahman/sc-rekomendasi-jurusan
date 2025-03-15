import streamlit as st
from models.kategori_model import get_kategori_has_pertanyaan
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
        
    if st.button("📝 Default Kategori Pertanyaan", use_container_width=True):
        table_kategori_has_pertanyan()
        st.rerun()  # Refresh 
        
  
   