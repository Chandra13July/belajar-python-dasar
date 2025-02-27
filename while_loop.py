# Belajar While-Loop

# data = ""

# # Perulangan akan berjalan selama data tidak bernilai "x"
# while data.lower() != "x":
#     print("Masuk perulangan")
#     data = input("Masukkan data (ketik 'x' untuk keluar): ")

# print("Perulangan selesai.")

while True:
    data = input("Masukkan data (ketik 'x' untuk keluar): ")
    
    if data.lower() == "x":  # Menggunakan lower() agar tidak case-sensitive
        print("Perulangan selesai.")
        break
    
    print(f"Anda memasukkan: {data}")
