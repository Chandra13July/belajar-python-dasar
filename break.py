# Belajar Break

# Menampilkan angka dari 1 hingga sebelum 50
for i in range(1, 100):
    if i % 50 == 0:
        break  # Hentikan perulangan saat i mencapai kelipatan 50
    print(i)

print("Perulangan berhenti karena mencapai 50.")
