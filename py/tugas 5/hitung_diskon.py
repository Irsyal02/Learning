def hitung_diskon(total_belanja):
    if total_belanja < 100000:
        return 0
    elif 100000 <= total_belanja <= 500000:
        return 0.1 * total_belanja
    else: 
        return 0.2 * total_belanja

def hitung_total_bayar(total_belanja, diskon):
    return total_belanja - diskon

def main():
    print("=== Penghitung Diskon Toko ===")
    
    try:
        total_belanja = float(input("Masukkan total belanja Anda (Rp): "))
        
        if total_belanja < 0:
            print("Total belanja tidak boleh negatif.")
            return
        
        diskon = hitung_diskon(total_belanja)
        total_bayar = hitung_total_bayar(total_belanja, diskon)
        
        print(f"Total belanja: Rp{total_belanja:,.2f}")
        print(f"Diskon: Rp{diskon:,.2f}")
        print(f"Total yang harus dibayar: Rp{total_bayar:,.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk total belanja.")

if __name__ == "__main__":
    main()
