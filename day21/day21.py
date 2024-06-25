# Definisi Class Mobil
class Mobil:
    def move(self):
        print("Berjalan di jalan raya")

# Definisi Class Pesawat
class Pesawat:
    def move(self):
        print("Terbang di udara")

# Definisi Class Kapal
class Kapal:
    def move(self):
        print("Berlayar di laut")

# Implementasi Objek dan Pemanggilan Method
mobil = Mobil()
pesawat = Pesawat()
kapal = Kapal()

# Pemanggilan metode move() untuk setiap objek
mobil.move()       # Output: Berjalan di jalan raya
pesawat.move()     # Output: Terbang di udara
kapal.move()       # Output: Berlayar di laut
