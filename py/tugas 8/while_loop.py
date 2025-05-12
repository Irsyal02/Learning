def main():
    total_ganjil = 0
    count = 0
    max_input = 8

    while count < max_input:
        try:
            angka = int(input("Masukkan angka (masukkan angka negatif untuk berhenti): "))
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
            continue

        if angka < 0:
            break


        if angka % 2 != 0:
            total_ganjil += angka

        count += 1

    print(f"Jumlah total angka ganjil yang dimasukkan: {total_ganjil}")

if __name__ == "__main__":
    main()