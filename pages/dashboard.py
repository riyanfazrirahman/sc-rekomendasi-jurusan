import streamlit as st
import pages.tabs.tab_aturan as tab_aturan
import pages.tabs.tab_jurusan as tab_jurusan
import pages.tabs.tab_kriteria as tab_kriteria

# Halaman Dashboard
st.title("📊 Dashboard")

# Tab 
tab1, tab2, tab3 = st.tabs(["Data Aturan", "Data Jurusan", "Data Kriteria"])

with tab1:
    tab_aturan.show()
    
with tab2:
    tab_jurusan.show()

with tab3:
    tab_kriteria.show()
