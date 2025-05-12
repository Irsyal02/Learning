# Tugas 2
jumlah = 0

while True:
    angka = int(input("Masukkan bilangan bulat positif (-1 untuk selesai): "))
    if angka == -1:
        break
    elif angka < -1:
        print("Masukkan angka yang valid!")
    else:
        jumlah += angka

print(f"Jumlah total angka yang dimasukkan adalah {jumlah}")
