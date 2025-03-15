import streamlit as st
import pages.tabs.tab_kategori_pertanyaan as tab_kategori_pertanyaan
import pages.tabs.tab_kategori as tab_kategori
import pages.tabs.tab_pertanyaan as tab_pertanyaan
import pages.tabs.tab_pertanyaan_kriteria as tab_pertanyaan_kriteria

# Halaman Dashboard
st.title("📊 Tabel Kategori")

# Tab 
tab1, tab2, tab3, tab4 = st.tabs(["Data Kategori & Pertanyaan", "Data Kategori", "Data Pertanyaan", "Data Pertanyaan & Kriteria"])

with tab1:
    tab_kategori_pertanyaan.show()

with tab2:
    tab_kategori.show()

with tab3:
    tab_pertanyaan.show()

with tab4:
    tab_pertanyaan_kriteria.show()
