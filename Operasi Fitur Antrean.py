from collections import deque

print("=== SIMULASI LANGKAH-LANGKAH OPERASI PADA FITUR ANTREAN (NOMOR 7) ===")

# Inisialisasi antrean menggunakan deque
antrean_mahasiswa = deque()

# Data mahasiswa sesuai nomor 5 pada lembar aktivitas:
# 1. Reysa Priatna
# 2. Taufickurahman Mirza
# 3. Budi Santoso
# 4. Dewi Lestari
# 5. Reysa Priatna

# LANGKAH 1: Penambahan data (Enqueue) - Reysa Priatna
print("\n--- Langkah 1: Enqueue Reysa Priatna ---")
antrean_mahasiswa.append("Reysa Priatna  (01)")
print("Data Yang Diproses : Reysa Priatna (01)")
print("Kondisi Struktur Data Setelah Operasi:", list(antrean_mahasiswa))

# LANGKAH 2: Penambahan data (Enqueue) - Taufickurahman Mirza
print("\n--- Langkah 2: Enqueue Taufickurahman Mirza ---")
antrean_mahasiswa.append("Taufickurahman Mirza (02)")
print("Data Yang Diproses : Taufickurahman Mirza (02)")
print("Kondisi Struktur Data Setelah Operasi:", list(antrean_mahasiswa))

# LANGKAH 3: Penambahan data (Enqueue) - Yahya Abiyu
print("\n--- Langkah 3: Enqueue Yahya Abiyu ---")
antrean_mahasiswa.append("Yahya Abiyu (03)")
print("Data Yang Diproses : Yahya Abiyu (03)")
print("Kondisi Struktur Data Setelah Operasi:", list(antrean_mahasiswa))

# LANGKAH 4: Penambahan data (Enqueue) - Prasetio Tri & Rafiq Alghifari
print("\n--- Langkah 4 & 5: Enqueue Prasetio Tri & Rafiq Alghifari ---")
antrean_mahasiswa.append("Prasetio Tri (04)")
antrean_mahasiswa.append("Rafiq Alghifari (05)")
print("Data Yang Diproses : Prasetio Tri (04), Rafiq Alghifari (05)")
print("Kondisi Struktur Data Setelah Operasi:", list(antrean_mahasiswa))

# LANGKAH 6: Penghapusan data (Dequeue / Melayani mahasiswa terdepan)
print("\n--- Langkah 6: Dequeue (Melayani Mahasiswa Terdepan) ---")
mahasiswa_dilayani = antrean_mahasiswa.popleft()
print(f"Data Yang Diproses : Melayani {mahasiswa_dilayani}")
print("Kondisi Struktur Data Setelah Operasi:", list(antrean_mahasiswa))

# LANGKAH 7: Melihat data terdepan (Peek / Front)
print("\n--- Langkah 7: Peek (Melihat Mahasiswa Terdepan) ---")
mahasiswa_terdepan = antrean_mahasiswa[0] if antrean_mahasiswa else "Kosong"
print(f"Data Yang Diproses : Melihat antrean terdepan")
print(f"Hasil Peek         : {mahasiswa_terdepan}")
print("Kondisi Struktur Data Setelah Operasi:", list(antrean_mahasiswa), "(Antrean tetap, tidak berubah)")