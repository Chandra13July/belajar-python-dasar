# Belajar Default Argument Value

def say_hello(first_name="Anonymous", last_name="Indo"):
    """Fungsi untuk menyapa dengan nama depan dan belakang (default tersedia)."""
    print(f"Hello, {first_name} {last_name}!")

# Memanggil fungsi dengan satu atau tanpa argumen
say_hello("Alief")  # last_name tetap menggunakan default "Indo"
say_hello()  # Menggunakan kedua nilai default
