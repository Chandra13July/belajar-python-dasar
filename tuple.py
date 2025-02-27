# Belajar Tuple

# Mendefinisikan tuple pelanggan
pelanggan = ("Alief", "Chandra", "Darmawan")

# Menampilkan data pelanggan berdasarkan indeks
print("Daftar Pelanggan:")
for i, nama in enumerate(pelanggan):
    print(f"{i + 1}. {nama}")
