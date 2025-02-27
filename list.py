# Belajar List

# Membuat List
nama = ["Alief", "Chandra", "Darmawan"]

# Menambah Data ke List
nama.append("Mary")

# Menampilkan seluruh data dalam list
print("Daftar Nama:", nama)

# Mengakses elemen List berdasarkan indeks
print("Nama pertama:", nama[0])
print("Nama kedua:", nama[1])
print("Nama ketiga:", nama[2])
print("Nama keempat:", nama[3])

# Menampilkan jumlah elemen dalam list
print("Jumlah elemen dalam list:", len(nama))

# Menghapus Data dari List
nama.remove("Chandra")
print("Setelah menghapus 'Chandra':", nama)

# Mengubah Data di List
nama[0] = "Chandra"
print("Setelah mengubah elemen pertama:", nama)
