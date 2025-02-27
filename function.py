# function.py

def say_hello(nama):
    """Fungsi untuk menyapa seseorang."""
    return f"Hello {nama}"

def total(*list_angka):
    """Fungsi untuk menjumlahkan angka dalam list_angka."""
    return sum(list_angka)  # Menggunakan sum() agar lebih ringkas
