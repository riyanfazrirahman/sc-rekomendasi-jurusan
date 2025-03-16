import pandas as pd

def buat_kode_terbaru(df, kolom=" ", prefix_default=" "):
    """
    Mengambil kode pertanyaan terakhir dari database dan menambah angka +1.
    Jika kosong, mulai dari prefix_default + '1' (contoh: P1).
    
    Parameters:
    - df: DataFrame yang berisi daftar pertanyaan
    - kolom: Nama kolom yang menyimpan kode pertanyaan
    - prefix_default: Awalan default jika tidak ditemukan prefix (default: " ")
    
    Returns:
    - String kode pertanyaan terbaru (misal: "F16" jika sebelumnya "F15")
    """
    if df is not None and not df.empty:
        # Cek apakah kolom ada di DataFrame
        if kolom not in df.columns:
            return f"{prefix_default}1"  # Kalau kolom tidak ada, pakai default

        kode_terakhir = df[kolom].iloc[-1]  # Ambil kode terakhir
        
        # Pisahkan prefix huruf dan angka
        prefix = ''.join(filter(str.isalpha, kode_terakhir))  # Ambil huruf (misal 'F')
        angka = ''.join(filter(str.isdigit, kode_terakhir))   # Ambil angka (misal '15')

        if angka.isdigit():
            return f"{prefix}{int(angka) + 1}"  # Tambah angka +1
        else:
            return f"{prefix}1"  # Jika tidak ada angka, mulai dari 1
    else:
        return f"{prefix_default}1"  # Jika database kosong, mulai dari P1
