# Menggunakan operator +
result = "Hello" + " " + "World"
text = "Hello World"
substring = text[0:5]  # Output: Hello
text = "Hello World"
position = text.find("World")  # Output: 6
text = "Hello World"
replaced = text.replace("World", "Python")  # Output: Hello Python
def gabungkan_string():
    str1 = input("Masukkan string pertama: ")
    str2 = input("Masukkan string kedua: ")
    print(str1 + str2)

def main():
    gabungkan_string()

if __name__ == "__main__":
    main()
