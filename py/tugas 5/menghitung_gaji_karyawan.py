def hitung_gaji_pokok(jam_kerja, gaji_per_jam):

    jam_reguler = min(jam_kerja, 40)
    return jam_reguler * gaji_per_jam

def hitung_lembur(jam_kerja, gaji_per_jam):

    jam_lembur = max(0, jam_kerja - 40)
    return jam_lembur * gaji_per_jam * 1.5

def hitung_total_gaji(gaji_pokok, gaji_lembur):

    return gaji_pokok + gaji_lembur


def main():
    print("=== Sistem Penghitung Gaji Karyawan ===")
    
    try:

        jam_kerja = float(input("Masukkan total jam kerja karyawan: "))
        gaji_per_jam = float(input("Masukkan gaji per jam (Rp): "))
        
        if jam_kerja < 0 or gaji_per_jam < 0:
            print("Jam kerja dan gaji per jam tidak boleh negatif.")
            return
        
        gaji_pokok = hitung_gaji_pokok(jam_kerja, gaji_per_jam)

        gaji_lembur = hitung_lembur(jam_kerja, gaji_per_jam)

        total_gaji = hitung_total_gaji(gaji_pokok, gaji_lembur)

        print(f"\nRincian Gaji Karyawan:")
        print(f"Gaji Pokok (40 jam pertama): Rp{gaji_pokok:,.2f}")
        print(f"Gaji Lembur (di atas 40 jam): Rp{gaji_lembur:,.2f}")
        print(f"Total Gaji: Rp{total_gaji:,.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk jam kerja dan gaji per jam.")

if __name__ == "__main__":
    main()
