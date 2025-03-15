import sqlite3
import json
import uuid
from datetime import datetime

def simpan_jawaban(jawaban_user):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # 🔥 Ambil hanya kode kriteria (tanpa pertanyaan)
    kriteria_terpilih = []
    for jawaban in jawaban_user.values():
        if isinstance(jawaban, list):  # Jika multiple choice (checkbox)
            kriteria_terpilih.extend(jawaban)
        else:  # Jika single choice (radio)
            kriteria_terpilih.append(jawaban)

    # 🔥 Konversi ke JSON hanya kode kriteria
    jawaban_json = json.dumps(kriteria_terpilih, sort_keys=True)

    # Debugging: Pastikan hanya kode kriteria yang disimpan
    print("DEBUG: Data yang disimpan ->", jawaban_json)

    # Cek apakah jawaban sudah ada di database
    cursor.execute("SELECT kode FROM riwayat_jawaban WHERE jawaban = ?", (jawaban_json,))
    hasil = cursor.fetchone()

    if hasil:
        conn.close()
        return hasil[0]  # Jika sudah ada, gunakan kode lama

    # Format kode unik lebih panjang
    kode_unik = str(uuid.uuid4())  # Full UUID (36 karakter dengan tanda -)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO riwayat_jawaban (kode, jawaban, timestamp) VALUES (?, ?, ?)",
                   (kode_unik, jawaban_json, timestamp))

    conn.commit()
    conn.close()

    return kode_unik  # Return kode unik baru jika belum ada sebelumnya


def get_all_history_jawaban():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()
    
    # Pastikan hanya mengambil 'kode' dan 'timestamp'
    cursor.execute("SELECT kode, timestamp FROM riwayat_jawaban ORDER BY timestamp DESC")
    hasil = cursor.fetchall()
    
    conn.close()
    return hasil


def ambil_jawaban_by_kode(kode):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    cursor.execute("SELECT jawaban FROM riwayat_jawaban WHERE kode = ?", (kode,))
    hasil = cursor.fetchone()
    
    conn.close()

    if hasil:
        return json.loads(hasil[0])  # Pastikan ini adalah JSON string yang bisa di-load
    else:
        return None


def hapus_jawaban_by_kode(kode):
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Hapus data berdasarkan kode unik
    cursor.execute("DELETE FROM riwayat_jawaban WHERE kode = ?", (kode,))
    
    conn.commit()
    conn.close()

