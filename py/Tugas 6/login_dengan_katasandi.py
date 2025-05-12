# Tugas 4
kata_sandi_benar = "Python123"
percobaan = 0
maks_percobaan = 3

while percobaan < maks_percobaan:
    kata_sandi = input("Masukkan kata sandi: ")
    if kata_sandi == kata_sandi_benar:
        print("Login berhasil!")
        break
    else:
        percobaan += 1
        print(f"Kata sandi salah. Percobaan {percobaan} dari {maks_percobaan}.")
        
if percobaan == maks_percobaan:
    print("Akun terkunci.")
