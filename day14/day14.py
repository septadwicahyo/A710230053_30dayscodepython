def menu():
    print("1. Cek Ganjil/Genap")
    print("2. Hitung Faktorial")
    print("3. Keluar")
    return input("Pilihan: ")

def cek_ganjil_genap():
    angka = int(input("Masukkan angka: "))
    print("Genap" if angka % 2 == 0 else "Ganjil")

def hitung_faktorial():
    angka = int(input("Masukkan angka: "))
    faktorial = 1
    for i in range(1, angka + 1):
        faktorial *= i
    print(f"Faktorial dari {angka}: {faktorial}")

def main():
    while True:
        pilihan = menu()
        if pilihan == "1":
            cek_ganjil_genap()
        elif pilihan == "2":
            hitung_faktorial()
        elif pilihan == "3":
            break

if __name__ == "__main__":
    main()
