import os

# Fungsi untuk menambahkan tugas ke dalam file
def tambah_tugas(nama_file, tugas):
    with open(nama_file, "a") as file:
        file.write(tugas + "\n")
    print(f"Tugas '{tugas}' telah ditambahkan.")

# Fungsi untuk menampilkan semua tugas
def lihat_tugas(nama_file):
    if not os.path.exists(nama_file):
        print("Tidak ada tugas untuk ditampilkan.")
        return
    with open(nama_file, "r") as file:
        tugas = file.readlines()
    if tugas:
        print("Daftar Tugas:")
        for i, t in enumerate(tugas, start=1):
            print(f"{i}. {t.strip()}")
    else:
        print("Tidak ada tugas dalam daftar.")

# Fungsi untuk menghapus tugas berdasarkan nomor
def hapus_tugas(nama_file, nomor_tugas):
    if not os.path.exists(nama_file):
        print("Tidak ada tugas untuk dihapus.")
        return
    with open(nama_file, "r") as file:
        tugas = file.readlines()
    if 0 < nomor_tugas <= len(tugas):
        tugas_yang_dihapus = tugas.pop(nomor_tugas - 1)
        with open(nama_file, "w") as file:
            file.writelines(tugas)
        print(f"Tugas '{tugas_yang_dihapus.strip()}' telah dihapus.")
    else:
        print("Nomor tugas tidak valid.")

# Fungsi utama untuk mengelola aplikasi to-do list
def main():
    nama_file = "todo_list.txt"
    while True:
        print("\nMenu To-Do List:")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4): ")
        
        if pilihan == "1":
            tugas = input("Masukkan tugas baru: ")
            tambah_tugas(nama_file, tugas)
        elif pilihan == "2":
            lihat_tugas(nama_file)
        elif pilihan == "3":
            lihat_tugas(nama_file)
            try:
                nomor = int(input("Masukkan nomor tugas yang akan dihapus: "))
                hapus_tugas(nama_file, nomor)
            except ValueError:
                print("Nomor tugas harus berupa angka.")
        elif pilihan == "4":
            print("Keluar dari aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
