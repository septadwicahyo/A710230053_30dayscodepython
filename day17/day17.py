def baca_produk(file_path):
    produk = []
    with open(file_path, "r") as file:
        for line in file:
            nama, harga = line.strip().split(',')
            produk.append((nama, float(harga)))
    return produk

def hitung_total(produk):
    total = sum(harga for _, harga in produk)
    return total

def simpan_invoice(produk, total, file_path):
    with open(file_path, "w") as file:
        file.write("Rincian Belanja:\n")
        for nama, harga in produk:
            file.write(f"{nama}: {harga}\n")
        file.write(f"Total: {total}\n")

# Contoh data produk
produk = [("Apel", 5000), ("Pisang", 3000), ("Jeruk", 7000)]
total = hitung_total(produk)
simpan_invoice(produk, total, "invoice.txt")

# Membaca dan menampilkan isi file invoice
with open("invoice.txt", "r") as file:
    print(file.read())
