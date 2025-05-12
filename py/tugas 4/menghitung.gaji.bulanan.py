upah_per_jam = {
    'A': 4000,
    'B': 5000,
    'C': 6000,
    'D': 7500
}
upah_lembur = 3000 
jam_normal = 48  

nama = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan karyawan (A, B, C, D): ").upper()
jam_kerja = int(input("Masukkan jumlah jam kerja dalam seminggu: "))

if golongan in upah_per_jam:
    upah = upah_per_jam[golongan]
else:
    print("Golongan tidak valid.")
    exit()

if jam_kerja <= jam_normal:
    gaji = jam_kerja * upah
else:
    gaji = (jam_normal * upah) + ((jam_kerja - jam_normal) * (upah + upah_lembur))

print(f"Nama Karyawan: {nama}")
print(f"Golongan: {golongan}")
print(f"Total Jam Kerja: {jam_kerja}")
print(f"Gaji Mingguan: Rp {gaji}")
