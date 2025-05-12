# Tugas 1
count_genap = 0

while True:
    angka = int(input("Masukkan bilangan bulat (-1 untuk selesai): "))
    if angka == -1:
        break
    if angka % 2 == 0:
        count_genap += 1

print(f"Banyaknya bilangan genap adalah {count_genap}")