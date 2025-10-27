def greet(nama, age, x):
    print("hello," + nama)
    print("nice to meet you " + str(age)) 
    return x+5

print (greet("world", 30, 10))


def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "nol gabisa lol "
    return a / b

print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Masukkan pilihan (+,-,*,/): ")

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if pilihan == '+':
    hasil = tambah(a, b)
    print(f"Hasil penjumlahan: {a} + {b} adalah {hasil}")
elif pilihan == '-':
    hasil = kurang(a, b)
    print(f"Hasil penjumlahan: {a} - {b} adalah {hasil}")
elif pilihan == '*':
    hasil = kali(a, b)
    print(f"Hasil penjumlahan: {a} * {b} adalah {hasil}")
elif pilihan == '/':
    hasil = bagi(a, b)
    print(f"Hasil penjumlahan: {a} / {b} adalah {hasil}")
else:
    print("Pilihan tidak valid.")