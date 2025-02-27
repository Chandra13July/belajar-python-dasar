# Program Management Kontak
import function

# Daftar kontak awal
daftar_kontak = [
    {
        "nama": "Chandra",
        "email": "code13july@gmail.com",
        "telepon": "081331551771"
    }
]

# Program utama
while True:
    print("\n=== Menu ===")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")
    
    menu = input("Pilih Menu: ")
    
    if menu == "0":
        print("Program selesai berjalan, sampai jumpa!")
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
        print("Kontak berhasil ditambahkan.")
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia, silakan pilih yang benar.")