# Rekomendasi Jurusan

## 📌 Deskripsi

Aplikasi ini adalah sistem rekomendasi jurusan berbasis web yang dibuat menggunakan **Streamlit** dan **SQLite**. Pengguna dapat menambahkan, mengedit, dan menghapus aturan rekomendasi berdasarkan minat dan jurusan.

## 🚀 Instalasi

Pastikan Anda sudah menginstal **Python 3.10+** di sistem Anda.

### 1. Install dependencies

```sh
pip install streamlit
```

```sh
pip install streamlit-agraph
```

### 2. Jalankan aplikasi

```sh
py -m streamlit run app.py
```

Aplikasi akan berjalan di **[localhost](http://localhost:8501/)** dan dapat diakses melalui **[browser](https://sc-rekomendasi-jurusan.streamlit.app/)**.

## 📂 Struktur Folder

```
rekomendasi_jurusan/
│── app.py               # File utama aplikasi
│── rekomendasi.db       # Database SQLite
│── config/..            # Configurasi Database
│── models/..            # Fungsi yang di gunakan
│── pages/
│   ├── home.py          # Halaman utama
│   ├── database.py      # Halaman database
│   ├── login.py         # Halaman login
└── README.md            # Dokumentasi proyek
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
