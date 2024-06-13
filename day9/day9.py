class mahasiswa():
    def __init__(self, nim, nama, angkatan, prodi):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.prodi = prodi

    def kartu_mahasiswa(self):
        print(f"Selamat datang {self.nama} {self.nim} {self.angkatan} {self.prodi} di kampus UMS ")

mahasiswa1 = mahasiswa('0053', 'septa', 2023, 'PTI')
mahasiswa1.kartu_mahasiswa()

mahasiswa2 = mahasiswa('0062', 'panji', 2023, 'PTI')
mahasiswa2.kartu_mahasiswa()

mahasiswa3 = mahasiswa('0055', 'sheva', 2023, 'PTI')
mahasiswa3.kartu_mahasiswa()
