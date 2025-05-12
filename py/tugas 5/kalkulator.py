def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Pembagian dengan nol tidak diperbolehkan."
    return a / b

def main():
    print("=== Kalkulator Operasi Dua Angka ===")
    
    try:

        a = float(input("Masukkan bilangan pertama (a): "))
        b = float(input("Masukkan bilangan kedua (b): "))
        

        print("Pilih operasi matematika:")
        print("1. tambah")
        print("2. kurang")
        print("3. kali")
        print("4. bagi")
        operasi = input("Masukkan nama operasi (tambah, kurang, kali, bagi): ").strip().lower()
        

        if operasi == "tambah":
            hasil = tambah(a, b)
        elif operasi == "kurang":
            hasil = kurang(a, b)
        elif operasi == "kali":
            hasil = kali(a, b)
        elif operasi == "bagi":
            hasil = bagi(a, b)
        else:
            print("Operasi tidak valid. Silakan coba lagi.")
            return
        

        print(f"Hasil operasi {operasi}: {hasil}")
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")

main()