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

Aplikasi akan berjalan di **localhost** dan dapat diakses melalui browser.

## 📂 Struktur Folder

```
rekomendasi_jurusan/
│── app.py               # File utama aplikasi
│── rekomendasi.db       # Database SQLite
│── pages/
│   ├── home.py          # Halaman utama
│   ├── database.py      # Halaman database
│   ├── login.py         # Halaman login
└── README.md            # Dokumentasi proyek
```

## 🎯 Fitur Utama

✅ Menambahkan aturan rekomendasi (minat & jurusan)\
✅ Mengedit data secara langsung di tabel\
✅ Menghapus aturan rekomendasi dengan checkbox\
✅ Sistem login dengan peran **admin** & **user**

## 📌 Teknologi yang Digunakan

- **Python** (Streamlit)
- **SQLite** (Database ringan)
- **Pandas** (Manajemen data)

---
