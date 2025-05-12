def hitung_nilai_akhir(nilai_ujian, nilai_tugas):

    return (nilai_ujian * 0.7) + (nilai_tugas * 0.3)

def main():
    print("=== Penghitung Nilai Akhir Siswa ===")

    try:

        nilai_ujian = float(input("Masukkan nilai ujian (0-100): "))
        nilai_tugas = float(input("Masukkan nilai tugas (0-100): "))
        
        if not (0 <= nilai_ujian <= 100) or not (0 <= nilai_tugas <= 100):
            print("Nilai harus berada dalam rentang 0-100.")
            return
        
        nilai_akhir = hitung_nilai_akhir(nilai_ujian, nilai_tugas)

        print(f"Nilai Akhir Anda: {nilai_akhir:.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk nilai ujian dan nilai tugas.")

if __name__ == "__main__":
    main()
