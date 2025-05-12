def main():

    print("Operasi pada List:")
    angka_list = [1, 2, 3, 4, 5]
    print("List awal:", angka_list)


    angka_list.append(6)

    angka_list.remove(3)
    print("List setelah penambahan dan penghapusan:", angka_list)


    print("\nOperasi pada Tuple:")
    warna_tuple = ("merah", "biru", "hijau")

    ada_kuning = "kuning" in warna_tuple
    print("Apakah 'kuning' ada di dalam tuple?", ada_kuning)


    print("\nOperasi pada Dictionary:")
    data_dict = {
        "nama": "Alice",
        "usia": 25,
        "pekerjaan": "Programmer"
    }
    print("Dictionary awal:", data_dict)

    data_dict["kota"] = "Jakarta"
    data_dict["usia"] = 26
    print("Dictionary setelah penambahan dan perubahan:", data_dict)

    print("\nOperasi pada Set:")
    angka_set = {1, 2, 3, 4}
    print("Set awal:", angka_set)


    angka_set.add(5)

    angka_set.remove(2)
    print("Set setelah penambahan dan penghapusan:", angka_set)

if __name__ == "__main__":
    main()