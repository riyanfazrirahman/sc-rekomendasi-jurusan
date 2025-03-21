import streamlit as st
from models.history_model import (
    ambil_jawaban_by_kode, 
    get_all_history_jawaban,
    get_by_id_user_history_jawaban, 
    hapus_jawaban_by_kode,
    update_user_id_dari_kode,
    ambil_user_id_dari_kode
)
from models.rekomendasi_model import get_recommendation
from pages.component.chart_tree import generate_tree

st.markdown("## 📜 Riwayat Jawaban")
st.markdown("---")

col_s, col_e = st.columns([1, 3])
with col_e:
    # Ambil semua riwayat jawaban dari database
    if st.session_state.get("logged_in"):
        user_id = st.session_state.get("user_id")
        role = st.session_state.get("role")

    # role = "admin"
    if role == "admin":
        riwayat_list = get_all_history_jawaban()
    else:
        riwayat_list = get_by_id_user_history_jawaban(user_id)
        
    col5, col6, col7 = st.columns([2,2,1])
    with col5:
        # Input pencarian
        search_query = st.text_input("🔍 Cari berdasarkan Kode:", "").strip().lower()
    with col6:
        # Input kode riwayat
        kode_unik_input = st.text_input("Masukkan Kode Unik")

    berhasil = None 
    pesan = ""
    with col7:
        # Beri jarak agar tombol tidak terlalu dekat
        st.markdown("""<p style="margin-top:1.7rem;"></p>""", unsafe_allow_html=True)

        if st.button("🔄 Gunakan Kode Ini", use_container_width=True):
            if kode_unik_input:  
                berhasil = update_user_id_dari_kode(kode_unik_input, user_id)

                if berhasil:
                    pesan = "✅ Data berhasil diperbarui dengan akun Anda!"
                    st.session_state["user_id"] = ambil_user_id_dari_kode(kode_unik_input)
                    st.rerun()  # Refresh UI setelah update
                else:
                    pesan = "❌ Kode tidak ditemukan atau sudah digunakan!"
            else:
                pesan = "⚠️ Masukkan kode unik terlebih dahulu!"

    # Tampilkan pesan di luar col7
    if pesan:
        if berhasil:
            st.success(pesan)
        else:
            st.error(pesan)
    
    # Filter hasil berdasarkan pencarian
    filtered_list = [item for item in riwayat_list if search_query in item[1].lower()] if search_query else riwayat_list

    # Konfigurasi Pagination
    ITEMS_PER_PAGE = 5  # Jumlah item per halaman
    if "page" not in st.session_state:
        st.session_state["page"] = 0

    total_pages = (len(filtered_list) - 1) // ITEMS_PER_PAGE + 1
    start_idx = st.session_state["page"] * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE

    hasil_rekomendasi= None
    data_riwayat={}
    massage = ""

    if not filtered_list:
        st.info("Tidak ada riwayat yang ditemukan.")
    else:
        # Menampilkan riwayat dengan pagination
        for username, kode, timestamp in filtered_list[start_idx:end_idx]:
            with st.container(border=True):
                col1, col2, col3, col4 = st.columns([4.5,2.5,3,2])

                with col1:
                    if st.button(f"🆔 **{kode}**", key=f"lihat_{kode}", use_container_width=True):
                        jawaban_terpilih = ambil_jawaban_by_kode(kode)

                        if jawaban_terpilih:
                            st.session_state["jawaban_user"] = jawaban_terpilih  # Load ke session
                            data_riwayat = jawaban_terpilih  
                            # Konversi jawaban_user ke data_riwayat (list kode kriteria)

                            # Dapatkan rekomendasi dari jawaban ini
                            hasil_rekomendasi = get_recommendation(data_riwayat)
                            if hasil_rekomendasi:
                                st.markdown("### 📊 Hasil Rekomendasi")
                                for jurusan, persen in sorted(hasil_rekomendasi.items(), key=lambda x: x[1], reverse=True):
                                    st.progress(persen / 100)
                                    st.write(f"**{jurusan}: {persen:.2f}%**")
                            else:
                                massage = "⚠️ Tidak ada rekomendasi yang sesuai."

                col2.button(f"📅 {timestamp}", key=f"timestamp_{kode}", disabled=True, use_container_width=True)

                col3.button(f"🙉 {username}", key=f"user_{kode}", disabled=True, use_container_width=True)

                with col4:
                    if st.button("🗑️ Hapus", key=f"hapus_{kode}", use_container_width=True):
                        hapus_jawaban_by_kode(kode)
                        st.success(f"✅ Riwayat dengan kode `{kode}` berhasil dihapus.")
                        st.rerun()
    # Pagination controls
    col_prev, col_page, col_next = st.columns([1, 3, 1])

    with col_prev:
        if st.session_state["page"] > 0:
            if st.button("⬅️ Prev", use_container_width=True):
                st.session_state["page"] -= 1
                st.rerun()

    with col_page:
        st.markdown(f"<p style='text-align: center;'>Halaman {st.session_state['page'] + 1} dari {total_pages}</p>", unsafe_allow_html=True)

    with col_next:
        if st.session_state["page"] < total_pages - 1:
            if st.button("Next ➡️", use_container_width=True):
                st.session_state["page"] += 1
                st.rerun()
with col_s:
    # Generate dan tampilkan pohon keputusan
    st.markdown("### 🌳 Pohon Keputusan")
    dot = generate_tree(data_riwayat)
    st.graphviz_chart(dot, use_container_width=True)


