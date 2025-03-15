import streamlit as st
from models.pertanyaan_model import get_pertanyaan_has_kriteria
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

    if st.button("📝 Default Pertanyaan Kriteria ", use_container_width=True):
        table_pertanyaan_has_kriteria()
        st.rerun()  # Refresh



