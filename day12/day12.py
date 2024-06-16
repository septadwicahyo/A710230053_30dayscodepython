def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak dapat membagi dengan nol!"
    return a / b

def tampilkan_menu():
    print("\nKalkulator Sederhana")
    print("====================")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

def input_angka():
    while True:
        try:
            angka = float(input("Masukkan angka: "))
            return angka
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1/2/3/4/5): ")

        if pilihan == "5":
            print("Terima kasih telah menggunakan kalkulator ini. Sampai jumpa!")
            break
        
        if pilihan not in ["1", "2", "3", "4"]:
            print("Pilihan tidak valid, silakan coba lagi.")
            continue
        
        print("\nInput Angka:")
        angka1 = input_angka()
        angka2 = input_angka()

        if pilihan == "1":
            hasil = tambah(angka1, angka2)
            operasi = "+"
        elif pilihan == "2":
            hasil = kurang(angka1, angka2)
            operasi = "-"
        elif pilihan == "3":
            hasil = kali(angka1, angka2)
            operasi = "*"
        elif pilihan == "4":
            hasil = bagi(angka1, angka2)
            operasi = "/"

        print(f"\nHasil: {angka1} {operasi} {angka2} = {hasil}")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
