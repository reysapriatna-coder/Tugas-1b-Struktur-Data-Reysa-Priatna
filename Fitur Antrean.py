from collections import deque

print("=== NOMOR 3: IMPLEMENTASI STRUKTUR DATA (KODE PROGRAM) ===")

# ==========================================
# 1. STRUKTUR DATA UNTUK FITUR ANTREAN (QUEUE)
# ==========================================
class AntreanMahasiswa:
    def __init__(self):
        # Menggunakan collections.deque untuk efisiensi operasi Queue O(1)
        self.antrean = deque()

    def penambahan_data(self, mahasiswa):
        """Operasi Penambahan Data (Enqueue)"""
        self.antrean.append(mahasiswa)

    def penghapusan_data(self):
        """Operasi Penghapusan Data (Dequeue)"""
        if not self.memeriksa_kondisi_kosong():
            return self.antrean.popleft()
        return "Antrean kosong!"

    def melihat_data_terdepan(self):
        """Operasi Melihat Data Terdepan (Peek / Front)"""
        if not self.memeriksa_kondisi_kosong():
            return self.antrean[0]
        return "Antrean kosong!"

    def memeriksa_kondisi_kosong(self):
        """Operasi Memeriksa Kondisi Kosong (Is_Empty)"""
        return len(self.antrean) == 0


# ==========================================
# 2. STRUKTUR DATA UNTUK FITUR UNDO (STACK)
# ==========================================
class FiturUndoStack:
    def __init__(self):
        # Menggunakan List Python untuk implementasi Stack LIFO
        self.stack = []

    def penambahan_data(self, aktivitas):
        """Operasi Penambahan Data (Push)"""
        self.stack.append(aktivitas)

    def penghapusan_data(self):
        """Operasi Penghapusan Data (Pop / Undo)"""
        if not self.memeriksa_kondisi_kosong():
            return self.stack.pop()
        return "Tidak ada aktivitas untuk di-undo!"

    def melihat_data_terdepan(self):
        """Operasi Melihat Data Terdepan (Peek / Top)"""
        if not self.memeriksa_kondisi_kosong():
            return self.stack[-1]
        return "Riwayat kosong!"

    def memeriksa_kondisi_kosong(self):
        """Operasi Memeriksa Kondisi Kosong (Is_Empty)"""
        return len(self.stack) == 0


# ==========================================
# DEMONSTRASI / CONTOH KODE UNTUK TAMPILAN TERMINAL
# ==========================================
if __name__ == "__main__":
    print("\n--- PENGUJIAN KELAS ANTREAN (QUEUE) ---")
    q = AntreanMahasiswa()
    q.penambahan_data("Reysa Priatna")
    print("1. Penambahan data berhasil.")
    print("2. Melihat data terdepan:", q.melihat_data_terdepan())
    print("3. Cek kondisi kosong:", q.memeriksa_kondisi_kosong())
    q.penghapusan_data()
    print("4. Penghapusan data (dequeue) selesai.")

    print("\n--- PENGUJIAN KELAS UNDO (STACK) ---")
    s = FiturUndoStack()
    s.penambahan_data("Menambahkan data mahasiswa")
    print("1. Penambahan data (push) berhasil.")
    print("2. Melihat data teratas:", s.melihat_data_terdepan())
    print("3. Cek kondisi kosong:", s.memeriksa_kondisi_kosong())
    s.penghapusan_data()
    print("4. Penghapusan data (pop/undo) selesai.")