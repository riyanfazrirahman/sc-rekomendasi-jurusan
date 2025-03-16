import streamlit as st
from models.pertanyaan_model import format_pertanyaan_kriteria
from models.history_model import simpan_jawaban
from models.rekomendasi_model import *
from pages.component.chart_tree import generate_tree

# Halaman Home
st.title( f"🎓Sistem Rekomendasi Jurusan Kuliah STMIK Palangkaraya" )
st.markdown("---")

# Inisialisasi tempat simpan jawaban di session_state
if "jawaban_user" not in st.session_state:
    st.session_state["jawaban_user"] = {}

if "kategori_index" not in st.session_state:
    st.session_state["kategori_index"] = 0

user_id = st.session_state.get("user_id", None)  # Ambil ID jika login

data = format_pertanyaan_kriteria()

def tampilkan_form():
    kategori_dict = {}

    for kode_kat, nama_kat, kode_p, pertanyaan, jenis_p, kode_k, nama_k in data:
        if nama_kat not in kategori_dict:
            kategori_dict[nama_kat] = {}
        if pertanyaan not in kategori_dict[nama_kat]:
            kategori_dict[nama_kat][pertanyaan] = {
                "jenis": jenis_p,
                "kriteria": [],
                "kode_kriteria": []
            }
        if kode_k and nama_k:
            kategori_dict[nama_kat][pertanyaan]["kriteria"].append(nama_k)
            kategori_dict[nama_kat][pertanyaan]["kode_kriteria"].append(kode_k)

    kategori_list = list(kategori_dict.keys())
    selected_kategori = kategori_list[st.session_state["kategori_index"]]
    st.header(f"📌 {selected_kategori}")
    st.markdown(f"<p style='text-align: center; margin-top: 1rem; '></p>",unsafe_allow_html=True)

    with st.container(border=True):
        pertanyaan_dict = kategori_dict[selected_kategori]
        for pertanyaan, info in pertanyaan_dict.items():
            st.subheader(f"{pertanyaan}")

            col_left, col_center, col_end = st.columns([0.2, 10, 0.1])
            st.markdown("---")
            with col_center:
                with st.container():
                    if info["jenis"] == "multiple":
                        if pertanyaan not in st.session_state["jawaban_user"]:
                            st.session_state["jawaban_user"][pertanyaan] = []
                        
                        selected_options = st.session_state["jawaban_user"][pertanyaan]
                        for i, kriteria in enumerate(info["kriteria"]):
                            kode_kriteria = info["kode_kriteria"][i]
                            if st.checkbox(kriteria, key=f"{selected_kategori}_{pertanyaan}_{kode_kriteria}",
                                        value=kode_kriteria in selected_options):
                                if kode_kriteria not in selected_options:
                                    selected_options.append(kode_kriteria)
                            else:
                                if kode_kriteria in selected_options:
                                    selected_options.remove(kode_kriteria)
                        st.session_state["jawaban_user"][pertanyaan] = selected_options
                        st.markdown(f"<p style='text-align: center; margin-top: 1rem; '></p>",unsafe_allow_html=True)

                    else:
                        options_dict = {info["kriteria"][i]: info["kode_kriteria"][i] for i in range(len(info["kriteria"]))}
                        selected_label = next((label for label, kode in options_dict.items() if kode == st.session_state["jawaban_user"].get(pertanyaan)), None)
                        radio_options = list(options_dict.keys())
                        selected_label = st.radio(
                            "Pilih salah satu:", 
                            radio_options,
                            index=radio_options.index(selected_label) if selected_label else None,
                            key=f"{selected_kategori}_{pertanyaan}"
                        )
                        st.session_state["jawaban_user"][pertanyaan] = options_dict.get(selected_label, None)
                        st.markdown(f"<p style='text-align: center; margin-top: 1rem; '></p>",unsafe_allow_html=True)

        
    st.markdown(f"<p style='text-align: center; margin-top: 2rem; '></p>",unsafe_allow_html=True)

    # Navigasi kategori
    col1, col2, col3, col4, col5 = st.columns([1, 1, 2,4, 1])
    with col1:
        st.button("Previous", use_container_width=True,
                  disabled=st.session_state["kategori_index"] == 0,
                  on_click=lambda: st.session_state.update(kategori_index=st.session_state["kategori_index"] - 1)
                  if st.session_state["kategori_index"] > 0 else None)
    with col2:
        st.button("Next", use_container_width=True,
                disabled=st.session_state["kategori_index"] >= len(kategori_list) - 1,  # Disable kalau mentok
                on_click=lambda: st.session_state.update(kategori_index=st.session_state["kategori_index"] + 1) 
                if st.session_state["kategori_index"] < len(kategori_list) - 1 else None)

    # Variabel untuk menyimpan pesan hasil_rekomendasi
    hasil_rekomendasi = None 
    data_riwayat={}
    warning_massage = ""
    success_massage = ""
    with col5:
        if st.button("Refresh", use_container_width=True):
            # Reset semua state yang relevan
            st.session_state["kategori_index"] = 0
            st.session_state["jawaban_user"] = {}
            # Bersihkan hasil_rekomendasi dan massage
            massage = ""
            hasil_rekomendasi = None
            data_riwayat = []
            # Streamlit akan otomatis rerender halaman karena state berubah

    with col3:
        # Hanya tampilkan tombol rekomendasi jika sudah di kategori terakhir
        if st.session_state["kategori_index"] == len(kategori_list) - 1:
            tombol_rekomendasi = st.button("🔍 Dapatkan Rekomendasi", use_container_width=True)
            if tombol_rekomendasi:
                kriteria_user = []
                for jawaban in st.session_state["jawaban_user"].values():
                    if isinstance(jawaban, list):
                        kriteria_user.extend(jawaban)
                    elif jawaban:
                        kriteria_user.append(jawaban)

                if kriteria_user:
                    kode_unik = simpan_jawaban(st.session_state["jawaban_user"], user_id)
                    print(f"🔍 DEBUG user_id: {user_id}")

                    success_massage = f"✅ Jawaban berhasil disimpan dengan kode: `{kode_unik}`"
                    # Konversi jawaban_user ke data_riwayat (list kode kriteria)
                    data_riwayat = kriteria_user  # Pastikan kriteria_user berupa list kode kriteria

                    hasil_rekomendasi = get_recommendation(kriteria_user)
                    
                    if not hasil_rekomendasi:
                        warning_massage =  "⚠️ Tidak ada rekomendasi yang sesuai."
                else:
                    warning_massage =  "⚠️ Silakan pilih minimal satu kriteria."

    # Tampilkan pesan setelah tombol diklik
    if success_massage:
        st.success(success_massage)
    if warning_massage:
        st.warning(warning_massage)

    # Tampilkan hasil rekomendasi di luar kolom tombol (di luar `col3`)
    if hasil_rekomendasi:
        st.markdown("### 📊 Hasil Rekomendasi")
        for jurusan, persen in sorted(hasil_rekomendasi.items(), key=lambda x: x[1], reverse=True):
            st.progress(persen / 100)
            st.write(f"**{jurusan}: {persen:.2f}%**")
        
        # Generate dan tampilkan pohon keputusan
        st.markdown("### 🌳 Pohon Keputusan")
        dot = generate_tree(data_riwayat)
        st.graphviz_chart(dot)

    current_page = st.session_state["kategori_index"] + 1
    total_pages = len(kategori_list)
    st.markdown(f"""<p style='text-align: center; margin-top: 3rem;'>Halaman {current_page} dari {total_pages}</p>""", unsafe_allow_html=True)

if "jawaban_user" not in st.session_state or not isinstance(st.session_state["jawaban_user"], dict):
    st.session_state["jawaban_user"] = {}

if data:
    tampilkan_form()
