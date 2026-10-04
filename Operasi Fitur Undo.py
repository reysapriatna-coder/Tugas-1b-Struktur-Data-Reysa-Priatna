print("=== SIMULASI LANGKAH-LANGKAH OPERASI PADA FITUR UNDO (NOMOR 9) ===")

# Inisialisasi stack untuk riwayat aktivitas (Undo)
riwayat_undo = []

# Data aktivitas sesuai nomor 6 pada lembar aktivitas:
# 1. 04/10/2026 - 1:00 | Menambahkan data mahasiswa Reysa Priatna
# 2. 04/10/2026 - 1:35 | Memperbarui status layanan Taufickurahman Mirza
# 3. 04/10/2026 - 2:00 | Menghapus data antrean Yahya Abiyu
# 4. 04/10/2026 - 2:15 | Mengubah jadwal loket pelayanan
# 5. 04/10/2026 - 2:30 | Menambahkan data mahasiswa Rafiq Alghifari

# LANGKAH 1: Penambahan data aktivitas (Push) - Aktivitas 1
print("\n--- Langkah 1: Push Aktivitas 1 ---")
aktivitas_1 = "04/10/2026 - 1:00 | Menambahkan data mahasiswa Reysa Priatna"
riwayat_undo.append(aktivitas_1)
print(f"Data Yang Diproses : {aktivitas_1}")
print("Kondisi Struktur Data Setelah Operasi:", riwayat_undo)

# LANGKAH 2: Penambahan data aktivitas (Push) - Aktivitas 2 & 3
print("\n--- Langkah 2 & 3: Push Aktivitas 2 & 3 ---")
aktivitas_2 = "04/10/2026 - 1:35 | Memperbarui status layanan Taufickurahman Mirza"
aktivitas_3 = "04/10/2026 - 2:00 | Menghapus data antrean Budi Santoso"
riwayat_undo.append(aktivitas_2)
riwayat_undo.append(aktivitas_3)
print("Data Yang Diproses : Aktivitas 2 dan Aktivitas 3 ditambahkan")
print("Kondisi Struktur Data Setelah Operasi:", riwayat_undo)

# LANGKAH 4: Penambahan data aktivitas (Push) - Aktivitas 4 & 5
print("\n--- Langkah 4 & 5: Push Aktivitas 4 & 5 ---")
aktivitas_4 = "04/10/2026 - 2:15 | Mengubah jadwal loket pelayanan"
aktivitas_5 = "04/10/2026 - 2:30 | Menambahkan data mahasiswa Rafiq Alghifari"
riwayat_undo.append(aktivitas_4)
riwayat_undo.append(aktivitas_5)
print("Data Yang Diproses : Aktivitas 4 dan Aktivitas 5 ditambahkan")
print("Kondisi Struktur Data Setelah Operasi:", riwayat_undo)

# LANGKAH 6: Penghapusan data (Pop / Undo aktivitas terakhir)
print("\n--- Langkah 6: Pop (Melakukan Undo pada Aktivitas Terakhir) ---")
aktivitas_dibatalkan = riwayat_undo.pop()
print(f"Data Yang Diproses : Membatalkan ({aktivitas_dibatalkan})")
print("Kondisi Struktur Data Setelah Operasi:", riwayat_undo)

# LANGKAH 7: Melihat data teratas (Peek / Top)
print("\n--- Langkah 7: Peek (Melihat Aktivitas Teratas Saat Ini) ---")
aktivitas_teratas = riwayat_undo[-1] if riwayat_undo else "Kosong"
print("Data Yang Diproses : Melihat aktivitas teratas (peek)")
print(f"Hasil Peek         : {aktivitas_teratas}")
print("Kondisi Struktur Data Setelah Operasi:", riwayat_undo, "(Stack tetap, tidak berubah)")