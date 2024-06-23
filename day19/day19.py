def hitung_kuadrat():
    while True:
        try:
            # Meminta input dari user
            bilangan = int(input("Masukkan bilangan bulat: "))
            # Menghitung kuadrat
            kuadrat = bilangan ** 2
            # Menampilkan hasil
            print(f"Kuadrat dari {bilangan} adalah {kuadrat}")
            break  # Keluar dari loop jika input valid
        except ValueError:
            # Menangani input yang tidak valid
            print("Input yang dimasukkan tidak valid! Silakan coba lagi.")

# Memanggil fungsi
hitung_kuadrat()
