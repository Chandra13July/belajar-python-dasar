# Program Management Kontak

# Fungsi untuk menampilkan daftar kontak
def display_kontak(daftar_kontak):
    print("\n=== Daftar Kontak ===")
    if not daftar_kontak:
        print("Belum ada kontak yang tersimpan.")
    for kontak in daftar_kontak:
        print("========================")
        print(f"Nama    : {kontak['nama']}")
        print(f"Email   : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")

# Fungsi untuk menambahkan kontak baru
def new_kontak():
    nama = input("Nama    : ")
    email = input("Email   : ")
    telepon = input("Telepon : ")
    
    kontak = {
        "nama": nama,
        "email": email,
        "telepon": telepon
    }
    return kontak

# Fungsi untuk menghapus kontak berdasarkan nomor telepon
def hapus_kontak(daftar_kontak):
    telepon = input("Masukkan No Telepon yang akan dihapus: ")
    
    index = -1
    for i, kontak in enumerate(daftar_kontak):
        if telepon == kontak["telepon"]:
            index = i
            break
    
    if index == -1:
        print("Kontak tidak ditemukan.")
    else:
        del daftar_kontak[index]
        print("Kontak berhasil dihapus.")

# Fungsi untuk mencari kontak berdasarkan nama
def cari_kontak(daftar_kontak):
    nama_yg_dicari = input("Masukkan Nama yang dicari: ")
    print("\n=== Hasil Pencarian ===")
    
    ditemukan = False
    for kontak in daftar_kontak:
        if nama_yg_dicari.lower() in kontak["nama"].lower():
            print("========================")
            print(f"Nama    : {kontak['nama']}")
            print(f"Email   : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")
            ditemukan = True
    
    if not ditemukan:
        print("Kontak tidak ditemukan.")