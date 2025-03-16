import streamlit as st
from models.insert_default import table_aturan
from models.kriteria_model import get_options_kriteria
from models.jurusan_model import get_options_jurusan
from models.aturan_model import *

def show():
    # Tampilkan DataFrame Aturan 
    st.header("📌 Daftar Aturan Rekomendasi")

    # Ambil data aturan
    df_aturan = get_all_aturan()

    # Ambil opsi dropdown
    kriteria_options = get_options_kriteria()
    jurusan_options = get_options_jurusan()

    # Konfigurasi kolom
    if not df_aturan.empty:
        edited_df = st.data_editor(
            df_aturan,
            num_rows="dynamic",
            column_config={
                "id_aturan": None,  # Sembunyikan ID
                "kode_kriteria": st.column_config.Column("Kode Kriteria"), # Ganti nama kolom
                "nama_kriteria": st.column_config.SelectboxColumn(
                    "Kriteria", # Ganti nama kolom
                    options=kriteria_options,  # Hanya kriteria yang belum ada
                    help="Pilih kriteria"
                ), 
                "kode_jurusan": st.column_config.Column("Kode Jurusan"), # Ganti nama kolom
                "nama_jurusan": st.column_config.SelectboxColumn(
                    "Jurusan", # Ganti nama kolom
                    options=jurusan_options, # Dropdown dengan daftar jurusan dari database
                    help="Pilih jurusan"
                ),
            },
            disabled=["id_aturan"],  # ID tidak bisa diedit
            hide_index=True,  # Sembunyikan index default Pandas
        )

        # **🔍 DETEKSI INSERT (Baris yang baru ditambahkan)**
        new_rows = edited_df[edited_df["id_aturan"].isna()]

        if not new_rows.empty:
            for _, row in new_rows.iterrows():
                add_aturan(row["nama_kriteria"], row["nama_jurusan"])

            st.success("Aturan baru berhasil ditambahkan!")
            st.rerun()  # Refresh 

      
        
        # 🔥 **Deteksi baris yang dihapus**
        deleted_rows = df_aturan[~df_aturan["id_aturan"].isin(edited_df["id_aturan"])]

        # **Jika ada yang dihapus, hapus dari database**
        if not deleted_rows.empty:
            for id_aturan in deleted_rows["id_aturan"]:
                delete_aturan(id_aturan)

            st.success("Aturan yang dihapus telah diperbarui!")
            st.rerun()  # Refresh 
            
    else:
        st.info("Belum ada aturan yang ditambahkan.")

     # Menambahkan jurusan baru
    col1, col2, col3 = st.columns([1, 1, 4])

    with col1:
        if st.button("📝 Default Aturan", use_container_width=True):
            table_aturan()
            st.rerun()  # Refresh 
    with col2:
        # Jika tombol ditekan, simpan perubahan ke database
        if not df_aturan.empty:
            if st.button("💾 Simpan Perubahan", use_container_width=True):
                for index, row in edited_df.iterrows():
                    id_aturan = row["id_aturan"]
                    nama_kriteria_baru = row["nama_kriteria"]
                    nama_jurusan_baru = row["nama_jurusan"]
                    update_aturan(id_aturan, nama_kriteria_baru, nama_jurusan_baru)
                        
                    st.success("Perubahan berhasil disimpan!")
                    st.rerun()  # Refresh 
