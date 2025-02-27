# Belajar Metode (Method) / Function

# List untuk menyimpan nama
nama = []

# Fungsi untuk mencetak daftar nama
def print_nama():
    print("\nDaftar Nama:")
    print("================")
    for data in nama:
        print(data)
    print("================")

# Menambahkan nama dan mencetak daftar nama
nama.append("Alief")
print_nama()

nama.append("Chandra")
print_nama()

nama.append("Darmawan")
print_nama()
