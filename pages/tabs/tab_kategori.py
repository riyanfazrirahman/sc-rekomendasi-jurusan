import streamlit as st
from models.kategori_model import get_all_kategori
from models.insert_default import table_kategori

def show():
    # Tampilkan DataFrame kategori
    st.header("📌 Daftar Kategori")

    df_kategori = get_all_kategori()
    st.dataframe(
        df_kategori, 
        use_container_width=True, 
        hide_index=True
    )
        
    if st.button("📝 Default Kategori", use_container_width=True):
        table_kategori()
        st.rerun()  # Refresh 
  
   