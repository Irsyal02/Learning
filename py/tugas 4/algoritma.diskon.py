total_pembelian = float(input("Masukkan total pembelian: "))

if total_pembelian > 100000:
    diskon = 0.20
elif 50000 <= total_pembelian <= 100000:
    diskon = 0.15
elif 10000 <= total_pembelian < 50000:
    diskon = 0.10
else:
    diskon = 0.0

jumlah_diskon = total_pembelian * diskon
total_setelah_diskon = total_pembelian - jumlah_diskon

print(f"Diskon: {diskon * 100}%")
print(f"Jumlah diskon: Rp {jumlah_diskon}")
print(f"Total setelah diskon: Rp {total_setelah_diskon}")
