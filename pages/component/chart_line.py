import sqlite3
import pandas as pd

def get_history_stats(group_by="day"):
    """
    Mengambil jumlah history rekomendasi berdasarkan hari, bulan, atau tahun.

    Args:
        group_by (str): "day", "month", atau "year" untuk menentukan gruping data.

    Returns:
        pd.DataFrame: Data jumlah history per periode.
    """
    conn = sqlite3.connect("rekomendasi.db")
    cursor = conn.cursor()

    query = """
        SELECT DATE(timestamp) as periode, COUNT(*) as jumlah_history
        FROM riwayat_jawaban
        GROUP BY DATE(timestamp)
        ORDER BY periode ASC
    """ if group_by == "day" else """
        SELECT strftime('%Y-%m', timestamp) as periode, COUNT(*) as jumlah_history
        FROM riwayat_jawaban
        GROUP BY strftime('%Y-%m', timestamp)
        ORDER BY periode ASC
    """ if group_by == "month" else """
        SELECT strftime('%Y', timestamp) as periode, COUNT(*) as jumlah_history
        FROM riwayat_jawaban
        GROUP BY strftime('%Y', timestamp)
        ORDER BY periode ASC
    """

    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    return pd.DataFrame(data, columns=["Periode", "Jumlah History"])
