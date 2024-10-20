

# NAMA : IRSAL RIZKI NASRUL FADILAH #
# NIM : 241351086 #
# KELAS : PAGI B #

def kalkulator_sederhana():

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    print("Hasil penjumlahan:", angka1 + angka2)
    print("Hasil pengurangan:", angka1 - angka2)
    print("Hasil perkalian:", angka1 * angka2)

    if angka2 != 0:
        print("Hasil pembagian:", angka1 / angka2)
    else:
        print("Tidak dapat membagi dengan nol.")