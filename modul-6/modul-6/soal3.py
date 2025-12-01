angka_list = []  

def tambah_angka():
    print("=== Tambah Angka ===")
    ulang = True
    while ulang:
        try:
            angka = int(input("Masukkan angka: "))
            angka_list.append(angka)
            print("Angka berhasil ditambahkan!")
            ulang = False
        except:
            print("Input tidak valid! Harus angka. Coba lagi.")

def tampilkan_angka():
    print("=== Daftar Angka ===")
    if len(angka_list) == 0:
        print("Belum ada angka.")
    else:
        for i in range(len(angka_list)):
            print("Indeks", i, ":", angka_list[i])

def ubah_angka():
    print("=== Ubah Angka ===")
    if len(angka_list) == 0:
        print("Belum ada angka untuk diubah.")
    else:
        tampilkan_angka()
        benar = False
        while not benar:
            try:
                indeks = int(input("Masukkan indeks angka yang ingin diubah: "))
                if indeks >= 0 and indeks < len(angka_list):
                    nilai_baru = int(input("Masukkan nilai baru: "))
                    angka_list[indeks] = nilai_baru
                    print("Angka berhasil diubah!")
                    benar = True
                else:
                    print("Indeks tidak valid. Coba lagi.")
            except:
                print("Input tidak valid! Masukkan angka saja.")

def hapus_angka():
    print("=== Hapus Angka ===")
    if len(angka_list) == 0:
        print("Belum ada angka untuk dihapus.")
    else:
        tampilkan_angka()
        benar = False
        while not benar:
            try:
                indeks = int(input("Masukkan indeks angka yang ingin dihapus: "))
                if indeks >= 0 and indeks < len(angka_list):
                    angka_list[indeks] = 0   
                    print("Angka dihapus (diubah menjadi 0).")
                    benar = True
                else:
                    print("Indeks tidak valid. Coba lagi.")
            except:
                print("Input tidak valid! Masukkan angka saja.")

def cek_pembagian_sama():
    print("=== Cek Pembagian Dua Bagian Sama ===")
    if len(angka_list) == 0:
        print("Belum ada angka untuk dicek.")
    else:
        total = 0
        for a in angka_list:
            total = total + a

        if total % 2 != 0:
            print("Total ganjil, tidak bisa dibagi dua sama besar.")
            print("Hasil: False")
        else:
            setengah = total // 2
            jumlah = 0
            bisa = False

            for a in angka_list:
                jumlah = jumlah + a
                if jumlah == setengah:
                    bisa = True

            if bisa == True:
                print("Bisa dibagi dua bagian sama besar.")
                print("Hasil: True")
            else:
                print("Tidak bisa dibagi dua bagian sama besar.")
                print("Hasil: False")

def menu():
    jalan = True
    while jalan:
        print("=== Program Dominic Szoboszlai ===")
        print("1. Tambah Angka")
        print("2. Tampilkan Angka")
        print("3. Ubah Angka")
        print("4. Hapus Angka")
        print("5. Cek Dua Bagian Sama")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_angka()
        elif pilihan == "2":
            tampilkan_angka()
        elif pilihan == "3":
            ubah_angka()
        elif pilihan == "4":
            hapus_angka()
        elif pilihan == "5":
            cek_pembagian_sama()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program ini!")
            jalan = False
        else:
            print("Pilihan tidak valid! Masukkan angka 1 sampai 6.")


menu()
