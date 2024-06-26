# Superclass Tiket
class Tiket:
    def __init__(self, jenis, harga):
        self.jenis = jenis
        self.harga = harga

    def hitung_total(self, jumlah):
        return self.harga * jumlah

# Subclass TiketBiasa
class TiketBiasa(Tiket):
    def __init__(self):
        super().__init__("Biasa", 50000)  # Harga tiket biasa Rp 50,000

# Subclass TiketVIP
class TiketVIP(Tiket):
    def __init__(self):
        super().__init__("VIP", 100000)  # Harga tiket VIP Rp 100,000

# Subclass TiketGold
class TiketGold(Tiket):
    def __init__(self):
        super().__init__("Gold", 150000)  # Harga tiket Gold Rp 150,000

# Fungsi utama untuk menghitung harga tiket
def hitung_harga_tiket():
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold) : ").strip().lower()
    jumlah_tiket = int(input("Masukkan jumlah tiket : "))

    if jenis_tiket == "biasa":
        tiket = TiketBiasa()
    elif jenis_tiket == "vip":
        tiket = TiketVIP()
    elif jenis_tiket == "gold":
        tiket = TiketGold()
    else:
        print("Jenis tiket tidak valid!")
        return

    total_harga = tiket.hitung_total(jumlah_tiket)
    print(f"Total Harga Tiket : Rp {total_harga}")

# Memanggil fungsi utama
hitung_harga_tiket()
