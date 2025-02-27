# Belajar Argument List

def jumlahkan(x, *list_angka):
    """Fungsi untuk menjumlahkan angka dalam list_angka."""
    total = sum(list_angka)  # Menggunakan sum() untuk menjumlahkan lebih ringkas
    print(f"Total dari {list_angka} = {total}")

# Memanggil fungsi dengan beberapa angka
jumlahkan(10, 10, 10, 10, 10)
