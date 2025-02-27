# Belajar Keyword Argument List

def create_html(tag, text, **attributes):
    """Fungsi untuk membuat elemen HTML dengan atribut tambahan."""
    # Membuat tag pembuka dengan atribut
    html = f"<{tag}"  
    for key, value in attributes.items():
        html += f" {key}='{value}'"

    # Menutup tag pembuka dan menambahkan teks di dalamnya
    html += f">{text}</{tag}>"
    return html

# Membuat berbagai elemen HTML
html1 = create_html("p", "Hello Python", style="paragraf")
html2 = create_html("a", "Ini Link", href="www.google.com", style="link")
html3 = create_html("div", "Ini Div", style="contoh")

# Menampilkan hasil
print(html1)
print(html2)
print(html3)
