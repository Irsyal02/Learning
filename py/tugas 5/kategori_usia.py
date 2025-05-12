def tentukan_kategori_usia(umur):
    if 0 <= umur <= 12:
        return "Anak-anak"
    elif 13 <= umur <= 17:
        return "Remaja"
    elif 18 <= umur <= 64:
        return "Dewasa"
    elif umur >= 65:
        return "Lansia"
    else:
        return "Umur tidak valid"


def main():
    print("=== Program Penentuan Kategori Usia ===")
    
    try:

        umur = int(input("Masukkan umur Anda: "))
        

        kategori = tentukan_kategori_usia(umur)
        

        print(f"Kategori usia Anda: {kategori}")
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat sebagai umur.")

if __name__ == "__main__":
    main()
