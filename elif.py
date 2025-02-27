# Belajar Elif (else if)

# Meminta input dari pengguna
menu_pilihan = input("Silakan pilih menu [1-3] atau tekan 'x' untuk keluar: ")

# Cek pilihan menu
if menu_pilihan == "1":
    print("Anda memilih menu 1")
elif menu_pilihan == "2":
    print("Anda memilih menu 2")
elif menu_pilihan == "3":
    print("Anda memilih menu 3")
elif menu_pilihan.lower() == "x":  # Menangani input huruf besar/kecil
    print("Program keluar")
else:
    print("Menu tidak tersedia")