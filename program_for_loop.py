# Membuat Program Menggunakan For-Loop, List, dan Range

# Meminta jumlah data yang ingin dimasukkan
banyak = int(input("Berapa banyak data? "))

# List untuk menyimpan data nama dan umur
nama = []
umur = []

# Loop untuk memasukkan data
for i in range(banyak):
    print(f"Data ke-{i+1}")
    input_nama = input("Nama  : ")
    input_umur = input("Umur  : ")

    nama.append(input_nama)
    umur.append(input_umur)  # Sebelumnya salah, harusnya ditambahkan ke list umur

print("\nData yang telah dimasukkan:")
print("============================")
# Loop untuk menampilkan data
for i in range(len(nama)):
    print(f"{nama[i]} berumur {umur[i]} tahun")
print("============================")
