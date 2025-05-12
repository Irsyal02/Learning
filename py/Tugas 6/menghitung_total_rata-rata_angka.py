# Tugas 5
total = 0
jumlah_data = 0

while True:
    angka = int(input("Masukkan angka (-1 untuk selesai): "))
    if angka == -1:
        break
    total += angka
    jumlah_data += 1

if jumlah_data == 0:
    print("Tidak ada data yang dimasukkan.")
else:
    rata_rata = total / jumlah_data
    print(f"Jumlah total angka: {total}")
    print(f"Rata-rata angka: {rata_rata}")
