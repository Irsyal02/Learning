def cetak_pola_persegi(ukuran):
    for i in range(ukuran):
        for j in range(1, ukuran + 1):
            print(j, end=' ')
        print() 

def main():
    ukuran = 5
    cetak_pola_persegi(ukuran)

if __name__ == "__main__":
    main()