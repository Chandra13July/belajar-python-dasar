# Belajar Method Return Value

def jumlahkan(*list_angka):
    """Fungsi untuk menjumlahkan angka dalam list_angka dan mengembalikan totalnya."""
    total = sum(list_angka)  # Menggunakan sum() agar lebih ringkas
    return list_angka, total

# Memanggil fungsi dan mengambil hasilnya
list_angka, total = jumlahkan(10, 10, 10, 10, 10)

# Menampilkan hasil secara efisien
for _ in range(5):  # Mengulang print sebanyak 5 kali
    print(f"Total dari {list_angka} = {total}")
