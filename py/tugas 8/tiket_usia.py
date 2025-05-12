def hitung_harga_tiket(usia, waktu_pemesanan):
 
    if usia < 12:
        harga_tiket = 25000
    elif 12 <= usia <= 60:
        harga_tiket = 50000
    else:
        harga_tiket = 30000
        
    if waktu_pemesanan < 12:
        diskon = 0.10 
    elif waktu_pemesanan > 18:
        diskon = 0.05 
    else:
        diskon = 0.00  


    harga_setelah_diskon = harga_tiket * (1 - diskon)
    return harga_setelah_diskon

def main():

    try:
        usia = int(input("Masukkan usia pelanggan: "))
        waktu_pemesanan = int(input("Masukkan waktu pemesanan (dalam jam, format 24 jam): "))

        if waktu_pemesanan < 0 or waktu_pemesanan > 23:
            print("Waktu pemesanan tidak valid. Harap masukkan waktu antara 0 dan 23.")
            return

        harga = hitung_harga_tiket(usia, waktu_pemesanan)

        print(f"Harga tiket yang harus dibayar: Rp {harga:.2f}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk usia dan waktu pemesanan.")

if __name__ == "__main__":
    main()