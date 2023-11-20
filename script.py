class Kelas:
    def __init__(self):
        self.siswa = {}

    def tambah_siswa(self, nama):
        self.siswa[nama] = False

    def bayar_kas(self, nama):
        if nama in self.siswa:
            self.siswa[nama] = True
            print(f"{nama} telah membayar kas.")
        else:
            print(f"{nama} tidak terdaftar sebagai siswa.")

    def tampilkan_absensi(self):
        print("=== Absensi ===")
        for nama, sudah_bayar in self.siswa.items():
            status = "Sudah Bayar" if sudah_bayar else "Belum Bayar"
            print(f"{nama}: {status}")

def main():
    kelas = Kelas()

    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Bayar Kas")
        print("3. Tampilkan Absensi")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            nama_siswa = input("Masukkan nama siswa: ")
            kelas.tambah_siswa(nama_siswa)
            print(f"{nama_siswa} telah ditambahkan ke dalam kelas.")

        elif pilihan == "2":
            nama_siswa = input("Masukkan nama siswa yang sudah membayar kas: ")
            kelas.bayar_kas(nama_siswa)

        elif pilihan == "3":
            kelas.tampilkan_absensi()

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
