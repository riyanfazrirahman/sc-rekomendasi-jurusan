import streamlit as st
from models.pertanyaan_model import get_all_pertanyaan
from models.insert_default import table_pertanyaan

def show():
    # Tampilkan DataFrame Pertanyaan
    st.header("📌 Daftar Pertanyaan")

    df_pertanyaan = get_all_pertanyaan()
    st.dataframe(
        df_pertanyaan, 
        use_container_width=True, 
        hide_index=True
    )
        
    if st.button("📝 Default Pertanyaan", use_container_width=True):
        table_pertanyaan()
        st.rerun()  # Refresh 
  
   