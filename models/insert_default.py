import sqlite3

# Default Input untuk Jurusan
def table_jurusan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    daftar_jurusan = [
        ("J1", "Teknik Informatika"),
        ("J2", "Sistem Informasi"),
        ("J3", "Manajemen Informatika")
    ]

    # Cek apakah tabel jurusan masih kosong
    cursor.execute("SELECT COUNT(*) FROM jurusan")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO jurusan (kode_jurusan, nama_jurusan) VALUES (?, ?)", daftar_jurusan)
        conn.commit()
        print("✅ Jurusan default berhasil dimasukkan!")
    else:
        print("⚠️ Jurusan sudah ada di database.")

    conn.close()

# Default Input untuk Kriteria
def table_kriteria():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    daftar_kriteria = [
        ("F1", "Jenjang Pendidikan Strata-1 (S1)"),
        ("F2", "Tertarik untuk membuat aplikasi komputer atau permainan."),
        ("F3", "Suka memecahkan masalah dengan menggunakan komputer."),
        ("F4", "Berminat untuk belajar bagaimana cara membuat perangkat lunak (software)."),
        ("F5", "Senang belajar tentang cara kerja sistem komputer."),
        ("F6", "Menyukai matematika dan berpikir logis."),
        ("F7", "Tertarik untuk bekerja dengan komputer dan teknologi terbaru."),
        ("F8", "Ingin tahu bagaimana cara melindungi data dan informasi dari ancaman di internet."),
        ("F9", "Tertarik untuk membuat aplikasi yang bisa digunakan di smartphone."),
        ("F10", "Senang jika bisa memecahkan masalah yang sulit menggunakan komputer."),
        ("F11", "Tertarik belajar cara mengembangkan teknologi yang digunakan sehari-hari."),
        ("F12", "Tertarik dengan perangkat keras komputer dan cara kerjanya."),
        ("F13", "Senang belajar tentang kecerdasan buatan dan robotika."),
        ("F14", "Tertarik mengembangkan teknologi baru yang dapat digunakan dalam berbagai industri."),
        ("F15", "Tertarik untuk bekerja di bidang teknologi yang terus berkembang."),
        ("F16", "Jenjang Pendidikan Strata-1 (S1)"),
        ("F17", "Tertarik untuk mengelola dan mengorganisir informasi di komputer."),
        ("F18", "Senang bekerja dengan data untuk membantu perusahaan atau organisasi."),
        ("F19", "Ingin belajar bagaimana teknologi bisa digunakan untuk mempermudah pekerjaan sehari-hari."),
        ("F20", "Suka membuat website atau aplikasi yang digunakan orang banyak."),
        ("F21", "Tertarik dengan bagaimana perusahaan menggunakan teknologi untuk menjalankan bisnis."),
        ("F22", "Senang menganalisis data untuk membantu orang mengambil keputusan penting."),
        ("F23", "Tertarik untuk belajar cara membuat aplikasi yang mempermudah pekerjaan orang."),
        ("F24", "Ingin tahu bagaimana cara kerja sistem yang digunakan di banyak perusahaan besar."),
        ("F25", "Senang jika bisa membantu orang dengan mengembangkan solusi berbasis teknologi."),
        ("F26", "Tertarik untuk mengetahui cara teknologi dapat membuat pekerjaan lebih efisien."),
        ("F27", "Senang mencari solusi berbasis teknologi untuk masalah bisnis."),
        ("F28", "Tertarik untuk membantu perusahaan atau organisasi mengelola data mereka dengan lebih baik."),
        ("F29", "Senang mencari solusi berbasis teknologi untuk masalah bisnis."),
        ("F30", "Ingin bekerja di bidang yang menggabungkan teknologi dengan kebutuhan bisnis."),
        ("F31", "Jenjang Pendidikan Diploma-3 (D3)"),
        ("F32", "Tertarik untuk memimpin proyek yang menggunakan teknologi."),
        ("F33", "Suka belajar cara menggunakan komputer untuk memecahkan masalah dalam bisnis."),
        ("F34", "Senang jika bisa membantu organisasi atau perusahaan untuk berkembang dengan teknologi."),
        ("F35", "Ingin tahu bagaimana cara membuat keputusan bisnis dengan bantuan data dan teknologi."),
        ("F36", "Tertarik belajar tentang bagaimana perusahaan mengelola informasi dan data mereka."),
        ("F37", "Senang memikirkan cara teknologi dapat meningkatkan pengalaman pelanggan."),
        ("F38", "Tertarik untuk belajar cara teknologi bisa meningkatkan cara kerja perusahaan."),
        ("F39", "Suka membantu orang untuk menggunakan teknologi dengan lebih baik dalam pekerjaan mereka."),
        ("F40", "Ingin belajar cara memimpin tim yang bekerja dengan teknologi di perusahaan."),
        ("F41", "Tertarik untuk menggunakan komputer untuk meningkatkan efisiensi bisnis."),
        ("F42", "Tertarik untuk mempelajari cara mengelola tim yang bekerja dengan teknologi."),
        ("F43", "Senang bekerja dengan data untuk membuat keputusan yang tepat dalam bisnis."),
        ("F44", "Ingin belajar bagaimana mengimplementasikan solusi teknologi untuk meningkatkan kinerja perusahaan."),
        ("F45", "Tertarik untuk merancang dan mengelola proyek yang menggunakan teknologi."),
    ]

    # Cek apakah sudah ada data di tabel kriteria
    cursor.execute("SELECT COUNT(*) FROM kriteria")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO kriteria (kode_kriteria, nama_kriteria) VALUES (?, ?)", daftar_kriteria)
        conn.commit()
        print("✅ Kriteria default berhasil dimasukkan!")
    else:
        print("⚠️ Kriteria sudah ada di database.")
    conn.close()

# Default Input untuk Aturan
def table_aturan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    aturan_awal = [
        # Kriteria untuk J1 (Teknik Informatika)
        (["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13", "F14", "F15"], "J1"),
        
        # Kriteria untuk J2 (Sistem Informasi)
        (["F16", "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24", "F25", "F26", "F27", "F28", "F29", "F30"], "J2"),
        
        # Kriteria untuk J3 (Manajemen Informatika)
        (["F31", "F32", "F33", "F34", "F35", "F36", "F37", "F38", "F39", "F40", "F41", "F42", "F43", "F44", "F45"], "J3"),
    ]

    # Cek apakah tabel aturan sudah ada data
    cursor.execute("SELECT COUNT(*) FROM aturan")
    if cursor.fetchone()[0] == 0:
        for kode_kriteria_list, kode_jurusan in aturan_awal:
            # Dapatkan id_jurusan dari kode_jurusan
            cursor.execute("SELECT id_jurusan FROM jurusan WHERE kode_jurusan = ?", (kode_jurusan,))
            id_jurusan = cursor.fetchone()

            if id_jurusan:  # Pastikan id_jurusan ditemukan
                id_jurusan = id_jurusan[0]

                for kode_kriteria in kode_kriteria_list:
                    # Dapatkan id_kriteria dari kode_kriteria
                    cursor.execute("SELECT id_kriteria FROM kriteria WHERE kode_kriteria = ?", (kode_kriteria,))
                    id_kriteria = cursor.fetchone()

                    if id_kriteria:  # Pastikan id_kriteria ditemukan
                        id_kriteria = id_kriteria[0]

                        # Insert ke tabel aturan (PERIKSA DULU APA SUDAH ADA)
                        cursor.execute("""
                            INSERT INTO aturan (id_kriteria, id_jurusan) 
                            SELECT ?, ? 
                            WHERE NOT EXISTS (
                                SELECT 1 FROM aturan WHERE id_kriteria = ? AND id_jurusan = ?
                            )
                        """, (id_kriteria, id_jurusan, id_kriteria, id_jurusan))

        conn.commit()
        print("✅ Aturan default berhasil dimasukkan!")
    else:
        print("⚠️ Aturan sudah ada di database.")
    conn.close()


def table_kategori():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    kategori_list = [
        ("K1", "Pengembangan Aplikasi dan Pemrograman"),
        ("K2", "Analisis dan Pemecahan Masalah Komputasi"),
        ("K3", "Teknologi dan Sistem Komputer"),
        ("K4", "Manajemen Data dan Sistem Informasi"),
        ("K5", "Kepemimpinan Teknologi dan Solusi Bisnis"),
    ]
    cursor.execute("SELECT COUNT(*) FROM kategori")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO kategori (kode_kategori, nama_kategori) VALUES (?, ?)", kategori_list)
        conn.commit()
        print("✅ Kategori default berhasil dimasukkan!")
    else:
        print("⚠️ Kategori sudah ada di database.")        
    conn.close()


# Default Input untuk Pertanyaaan
def table_pertanyaan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Data default pertanyaan
    pertanyaan_list = [
        ("P1", "Apakah Anda tertarik untuk membuat aplikasi komputer, permainan, atau website?", "multiple"),
        ("P2", "Apakah Anda suka memecahkan masalah dengan menggunakan komputer?", "single"),
        ("P3", "Apakah Anda berminat untuk belajar cara membuat perangkat lunak (software)?", "single"),
        ("P4", "Apakah Anda senang belajar tentang cara kerja sistem dan perangkat keras komputer?", "multiple"),
        ("P5", "Apakah Anda menyukai matematika, berpikir logis, dan pemecahan masalah yang kompleks?", "multiple"),
        ("P6", "Apakah Anda tertarik untuk mempelajari keamanan data dan cara melindungi informasi dari ancaman di internet?", "single"),
        ("P7", "Apakah Anda tertarik dengan kecerdasan buatan, robotika, dan teknologi masa depan?", "multiple"),
        ("P8", "Apakah Anda senang bekerja dengan data untuk membantu pengambilan keputusan dalam organisasi?", "single"),
        ("P9", "Apakah Anda tertarik dengan bagaimana perusahaan menggunakan teknologi untuk menjalankan bisnis?", "single"),
        ("P10", "Apakah Anda ingin mengetahui cara kerja sistem informasi yang digunakan di banyak perusahaan besar?", "single"),
        ("P11", "Apakah Anda tertarik untuk mencari solusi berbasis teknologi untuk masalah bisnis?", "multiple"),
        ("P12", "Apakah Anda tertarik untuk memimpin proyek teknologi dan mengelola tim yang bekerja dengan teknologi?", "multiple"),
        ("P13", "Apakah Anda senang membantu organisasi berkembang dengan memanfaatkan teknologi?", "single"),
        ("P14", "Apakah Anda tertarik mempelajari cara teknologi dapat meningkatkan efisiensi dan pengalaman pelanggan?", "multiple"),
        ("P15", "Apakah Anda lebih tertarik pada jenjang pendidikan Strata-1 (S1) atau Diploma-3 (D3)?", "single"),
    ]

    cursor.execute("SELECT COUNT(*) FROM pertanyaan")
    if cursor.fetchone()[0] == 0:
        # Masukkan data default jika belum ada
        cursor.executemany("INSERT INTO pertanyaan (kode_pertanyaan, pertanyaan, jenis_pertanyaan) VALUES (?, ?, ?);", pertanyaan_list)

        # Simpan perubahan & tutup koneksi
        conn.commit()
        print("✅ Pertanyaan default berhasil dimasukkan!")
    else:
        print("⚠️ Pertanyaan sudah ada di database.")
    conn.close()


def table_kategori_has_pertanyan():
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    data = [
        ("K1", "P1"), ("K1", "P3"), ("K1", "P7"),
        ("K2", "P2"), ("K2", "P5"), ("K2", "P6"),
        ("K3", "P4"), ("K3", "P6"), ("K3", "P7"),
        ("K4", "P8"), ("K4", "P9"), ("K4", "P10"), ("K4", "P11"),
        ("K5", "P11"), ("K5", "P12"), ("K5", "P13"), ("K5", "P14"),
    ]

    cursor.execute("SELECT COUNT(*) FROM kategori_has_pertanyaan")
    if cursor.fetchone()[0] == 0:
        for kode_kategori, kode_pertanyaan in data:
            cursor.execute("""
                INSERT INTO kategori_has_pertanyaan (id_kategori, id_pertanyaan)
                VALUES (
                    (SELECT id_kategori FROM kategori WHERE kode_kategori = ?),
                    (SELECT id_pertanyaan FROM pertanyaan WHERE kode_pertanyaan = ?)
                )
            """, (kode_kategori, kode_pertanyaan))
        conn.commit()
        print("✅ Relasi kategori_has_pertanyaan default berhasil dimasukkan!")
    else:
        print("⚠️ Relasi kategori_has_pertanyaan sudah ada di database.")
    conn.close()

    
def table_pertanyaan_has_kriteria():
    # Koneksi ke database SQLite
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    # Data relasi kriteria dan pertanyaan (kode_kriteria, kode_pertanyaan)
    kriteria_pertanyaan = [
        ("F1", "P15"), ("F30", "P15"),
        ("F2", "P1"), ("F19", "P1"),
        ("F3", "P2"), ("F10", "P2"),
        ("F4", "P3"),
        ("F5", "P4"), ("F12", "P4"),
        ("F6", "P5"),
        ("F8", "P6"),
        ("F13", "P7"), ("F14", "P7"),
        ("F17", "P8"), ("F21", "P8"),
        ("F20", "P9"),
        ("F23", "P10"),
        ("F26", "P11"), ("F28", "P11"), ("F29", "P11"),
        ("F31", "P12"), ("F41", "P12"),
        ("F33", "P13"),
        ("F25", "P14"), ("F36", "P14"), ("F37", "P14"),
    ]

    cursor.execute("SELECT COUNT(*) FROM pertanyaan_has_kriteria")
    if cursor.fetchone()[0] == 0:
        # Masukkan data ke dalam pertanyaan_has_kriteria
        for kode_kriteria, kode_pertanyaan in kriteria_pertanyaan:
            # Ambil id_kriteria dari tabel kriteria berdasarkan kode_kriteria
            cursor.execute("SELECT id_kriteria FROM kriteria WHERE kode_kriteria = ?", (kode_kriteria,))
            id_kriteria_result = cursor.fetchone()
            
            # Ambil id_pertanyaan dari tabel pertanyaan berdasarkan kode_pertanyaan
            cursor.execute("SELECT id_pertanyaan FROM pertanyaan WHERE kode_pertanyaan = ?", (kode_pertanyaan,))
            id_pertanyaan_result = cursor.fetchone()

            if id_kriteria_result and id_pertanyaan_result:  # Jika keduanya ditemukan
                cursor.execute("""
                    INSERT INTO pertanyaan_has_kriteria (id_pertanyaan, id_kriteria)
                    VALUES (?, ?)
                """, (id_pertanyaan_result[0], id_kriteria_result[0]))

        # Simpan perubahan & tutup koneksi
        conn.commit()
        print("✅ Relasi pertanyaan_has_kriteria default berhasil dimasukkan!")
    else:
        print("⚠️ Relasi pertanyaan_has_kriteria sudah ada di database.")
    conn.close()