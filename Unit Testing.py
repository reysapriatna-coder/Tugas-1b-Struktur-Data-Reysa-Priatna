from collections import deque
import unittest

print("=== PENGUJIAN UNIT TESTING PADA FITUR ANTREAN (NOMOR 12) ===")

# Implementasi Kelas Antrean Layanan Mahasiswa
class AntreanLayanan:
    def __init__(self):
        self.antrean = deque()

    def enqueue(self, mahasiswa):
        """Operasi Penambahan Data"""
        self.antrean.append(mahasiswa)

    def dequeue(self):
        """Operasi Penghapusan Data"""
        if not self.is_empty():
            return self.antrean.popleft()
        return None

    def peek(self):
        """Operasi Melihat Data Terdepan"""
        if not self.is_empty():
            return self.antrean[0]
        return None

    def is_empty(self):
        """Operasi Memeriksa Kondisi Kosong"""
        return len(self.antrean) == 0


# Kelas Unit Testing untuk Menguji Fitur Antrean dengan Berbagai Input
class TestAntreanLayanan(unittest.TestCase):

    def setUp(self):
        """Inisialisasi objek sebelum setiap test case dijalankan"""
        self.loket = AntreanLayanan()

    def test_1_penambahan_data_enqueue(self):
        """Pengujian Operasi Penambahan Data dengan Input Berbeda"""
        print("\n[TEST] Menjalankan Pengujian Penambahan Data (Enqueue)...")
        self.loket.enqueue("Reysa Priatna")
        self.loket.enqueue("Taufickurahman Mirza")
        
        self.assertEqual(len(self.loket.antrean), 2)
        self.assertEqual(self.loket.antrean[0], "Reysa Priatna")
        self.assertEqual(self.loket.antrean[1], "Taufickurahman Mirza")
        print("Input: 'Reysa Priatna', 'Taufickurahman Mirza' -> Berhasil ditambahkan.")

    def test_2_penghapusan_data_dequeue(self):
        """Pengujian Operasi Penghapusan Data dengan Input Berbeda"""
        print("\n[TEST] Menjalankan Pengujian Penghapusan Data (Dequeue)...")
        self.loket.enqueue("Reysa Priatna")
        self.loket.enqueue("Taufickurahman Mirza")

        dihapus = self.loket.dequeue()
        self.assertEqual(dihapus, "Reysa Priatna")
        self.assertEqual(len(self.loket.antrean), 1)
        self.assertEqual(self.loket.peek(), "Taufickurahman Mirza")
        print(f"Input/Operasi Dequeue berhasil menghapus: {dihapus}")

    def test_3_melihat_data_terdepan_peek(self):
        """Pengujian Operasi Melihat Data Terdepan dengan Input Berbeda"""
        print("\n[TEST] Menjalankan Pengujian Melihat Data Terdepan (Peek)...")
        self.loket.enqueue("Reysa Priatna")
        self.loket.enqueue("Taufickurahman Mirza")
        
        terdepan = self.loket.peek()
        self.assertEqual(terdepan, "Reysa Priatna")
        # Pastikan ukuran antrean tidak berubah saat peek
        self.assertEqual(len(self.loket.antrean), 2)
        print(f"Input: Data antrean aktif -> Data terdepan adalah: {terdepan}")

    def test_4_memeriksa_kondisi_kosong_is_empty(self):
        """Pengujian Operasi Memeriksa Kondisi Kosong dengan Input Berbeda"""
        print("\n[TEST] Menjalankan Pengujian Kondisi Kosong (Is_Empty)...")
        # Saat baru diinisialisasi
        self.assertTrue(self.loket.is_empty())
        print("Input: Antrean baru -> Kondisi kosong: True")
        
        # Setelah ditambah data
        self.loket.enqueue("Mahasiswa X")
        self.assertFalse(self.loket.is_empty())
        print("Input: Ditambah 'Mahasiswa X' -> Kondisi kosong: False")


if __name__ == '__main__':
    # Menjalankan unit testing secara otomatis
    unittest.main(argv=['first-arg-is-ignored'], exit=False)