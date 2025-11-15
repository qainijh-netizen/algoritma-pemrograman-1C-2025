data_kunjungan = []
nomor_antrian = 1  

def tambah_data():
    global nomor_antrian
    print("=== Tambah Data Pengunjung ===")
    nama_pengunjung = input("Masukkan nama pengunjung: ").strip()
    nama_santri = input("Masukkan nama santri yang dijenguk: ").strip()

    while True:
        daerah = input("Masukkan daerah asal pengunjung (sumatra/kalimantan/jawa): ").strip().lower()
        if daerah in ["sumatra", "kalimantan", "jawa"]:
            break
        else:
            print("Input daerah tidak valid! Harus 'sumatra', 'kalimantan', atau 'jawa'. Coba lagi")

    data_kunjungan.append([nomor_antrian, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan dengan nomor antrian: {nomor_antrian}")
    nomor_antrian += 1

def tampilkan_data():
    if not data_kunjungan:
        print("Belum ada data kunjungan")
        return

    print("=== Daftar Kunjungan Santri ===")
    urutan_daerah = ["sumatra", "kalimantan", "jawa"]

    for daerah in urutan_daerah:
        print(f"--- Pengunjung dari {daerah} ---")
        ditemukan = False
        for data in data_kunjungan:
            if data[3] == daerah:
                print(f"nomor antri: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]} | Daerah: {data[3]}")
                ditemukan = True
        if not ditemukan:
            print("Tidak ada pengunjung dari daerah ini.")

def hapus_data():
    if not data_kunjungan:
        print("Tidak ada data untuk dihapus.")
        return

    print("=== Hapus Data Pengunjung ===")
    while True:
        try:
            id_hapus = int(input("Masukkan nomor antrian yang ingin dihapus: "))
            break
        except ValueError:
            print("Input harus berupa angka. Coba lagi")

    for data in data_kunjungan:
        if data[0] == id_hapus:
            data_kunjungan.remove(data)
            print(f"Data dengan nomor antrian {id_hapus} berhasil dihapus.")
            return

    print("Nomor antrian tidak ditemukan! Coba lagi.")

def menu():
    while True:
        print("=== Sistem Kunjungan Santri ===")
        print("1. Tambah Data Pengunjung")
        print("2. Tampilkan Daftar Pengunjung")
        print("3. Hapus Data Pengunjung")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            hapus_data()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem kunjungan santri!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih angka 1-4.")

menu()
