# Belajar Continue

# Menampilkan bilangan ganjil dari 1 hingga 99
for i in range(1, 100):
    if i % 2 == 0:
        continue  # Lewati bilangan genap
    print(i)
