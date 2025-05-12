# Tugas 3
kata_rahasia = "python"
while True:
    tebakan = input("Tebak kata rahasia: ")
    if tebakan.lower() == kata_rahasia:
        print("Selamat! Tebakan Anda benar.")
        break
    else:
        print("Tebakan salah, coba lagi!")
