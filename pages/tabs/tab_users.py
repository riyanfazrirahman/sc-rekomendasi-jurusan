import streamlit as st
from models.auth_model import get_all_users, update_user_roles
from models.history_model import get_by_id_user_history_jawaban

def show():
    # Tampilkan DataFrame Pengguna
    st.header("📌 Daftar Pengguna")

    df_users = get_all_users()  # Ambil daftar user

    if df_users.empty:
        st.warning("⚠️ Tidak ada pengguna dalam database!")
        return 

    # Tambahkan kolom jumlah history per user
    df_users["Jumlah Riwayat"] = df_users["ID"].apply(
        lambda user_id: len(get_by_id_user_history_jawaban(user_id))
    )
    
    col1, col2 = st.columns([2, 1])
    with col1:
        edited_df = st.data_editor(
            df_users,
            num_rows="dynamic",
            disabled=["ID", "Username", "Riwayat"],  # ID, Username, dan History tidak bisa diedit
            column_config={
                "Role": st.column_config.SelectboxColumn(
                    "Role", options=["admin", "user"]
                )
            },
        )

    if st.button("💾 Simpan Perubahan", use_container_width=False):
        update_user_roles(edited_df)
        st.success("✅ Perubahan berhasil disimpan!")
        st.rerun()  # Refresh halaman