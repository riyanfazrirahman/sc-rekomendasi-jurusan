# Rekomendasi Jurusan

## 📌 Deskripsi

Aplikasi ini adalah sistem rekomendasi jurusan berbasis web yang dibuat menggunakan **Streamlit** dan **SQLite**. Pengguna dapat menambahkan, mengedit, dan menghapus aturan rekomendasi berdasarkan minat dan jurusan.

## ✨ Tujuan

Membantu calon mahasiswa dalam memilih jurusan yang sesuai dengan minat, bakat, dan kemampuan sekaligus mengurangi tingkat ketidaktepatan dalam pemilihan jurusan kuliah dengan menggunakan metode forward chaining.

## 👥 Kelompok 5 - Kecerdasan Buatan

| Status   | Name                | NIM           | University          | Media                                                                       | GitHub                                        |
| -------- | ------------------- | ------------- | ------------------- | --------------------------------------------------------------------------- | --------------------------------------------- |
| `Active` | Riyan Fazri Rahman  | `C2255201005` | STMIK Palangka Raya | [LinkedIn](https://www.linkedin.com/in/riyan-fazri-rahman/)                 | [GitHub](https://github.com/riyanfazrirahman) |
| `Active` | Alif Rahmatullah L. | `C2255201029` | STMIK Palangka Raya | [LinkedIn](https://www.linkedin.com/in/alif-rahmatullah-lesmana-565028311/) | [GitHub](https://github.com/Peparrepair)      |
| `Active` | Rif'ad Amin Jayadi  | `C2255201018` | STMIK Palangka Raya | -                                                                           | [GitHub](https://github.com/)                 |
| `Active` | Nazia Fitra Aini    | `C2255201002` | STMIK Palangka Raya | -                                                                           | [GitHub](https://github.com/)                 |
| `Active` | Oga Luisca MIka S.  | `C2255201016` | STMIK Palangka Raya | -                                                                           | [GitHub](https://github.com/)                 |

---

## 🚀 Instalasi

Pastikan Anda sudah menginstal **Python 3.10+** di sistem Anda.

### 1. Install dependencies

```sh
pip install streamlit
```

```sh
pip install graphviz
```

```sh
pip install bcrypt
```

### 2. Jalankan aplikasi

```sh
py -m streamlit run app.py
```

Aplikasi akan berjalan di **[localhost](http://localhost:8501/)** dan dapat diakses melalui **[browser](https://sc-rekomendasi-jurusan-app.streamlit.app/)**.

## 📂 Struktur Folder

```
rekomendasi_jurusan/
│── app.py                  # File utama aplikasi
│── rekomendasi.db          # Database SQLite
│── config/..               # Configurasi Database
│── models/..               # Fungsi yang di gunakan
│── pages/
│   ├── component/..        # Tab dashboard
│   ├── tabs/..             # Tab dashboard
│   ├── home.py             # Halaman utama
│   ├── dashboard.py        # Halaman dashboard
│   ├── form_rekomendasi.py # Halaman form rekomendasi
│   ├── tabel_rekomendasi.py# Halaman daftar aturan, kriteria dan jurusan
│   ├── tabel_pertanyaan.py # Halaman daftar pertanyaan
│   ├── tabel_users.py      # Halaman daftar pengguna
│   ├── auth.py             # Halaman login & register
│── requirements.txt        # Fungsi yang di gunakan
└── README.md               # Dokumentasi proyek
```

## 🎯 Fitur Utama

✅ Memberikan Rekomendasi (%)\
✅ Menambahkan juruasan, kreteria, dan aturan\
✅ Mengedit data tabel\
✅ Menghapus data\
✅ Sistem login dengan peran **admin**

## 📌 Teknologi yang Digunakan

- **Python** (Streamlit)
- **SQLite** (Database ringan)
- **Pandas** (Manajemen data)

---
