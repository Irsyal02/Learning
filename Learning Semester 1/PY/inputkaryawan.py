nama = (input("masukan nama karyawam : "))
jjk = int(input("masukan jumlah jam kerja: "))

if jjk < 48 :
    upahtotal = jjk * 2000
else:
    jamlembur = jjk - 48
    upahlembur = jamlembur * 3000
    upahnormal = 48 * 2000
    upahtotal = upahnormal + upahlembur
print("nama karyawan", nama)
print("jumlah upah", upahtotal)
