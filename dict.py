# Belajar Tipe Data Dictionary

# Membuat dictionary customer
customer = {
    "Name": "Chandra",
    "Age": 20,
    "Address": "Jatim"
}

# Mengakses nilai dari dictionary
name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

# Menambahkan dan memperbarui data dalam dictionary
customer["Company"] = "X"
customer["Name"] = "Alief Chandra"

# Menghapus data dari dictionary
del customer["Address"]

# Menampilkan seluruh data dalam dictionary
print("Informasi Customer:")
for key, value in customer.items():
    print(f"{key}: {value}")
