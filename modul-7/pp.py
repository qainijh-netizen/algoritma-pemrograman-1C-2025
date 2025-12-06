kupon = {
    "DISC10": 10,
    "HEMAT20": 20,
    "SALE30": 30
}
# tnp diskon, sprt di kasir
def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        print("===== Daftar Kupon =====")
        for kode, diskon in kupon.items():
            print(f"Kode: {kode}, Diskon: {diskon}%")
        print("========================")


def proses_transaksi():
    # Input total belanja
    while True:
        try:
            total = float(input("Masukkan total belanja: "))
            break
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

    print("Jika tidak punya kupon, tekan ENTER.")
    kode = input("Masukkan kode kupon: ").strip()

    if kode == "":
        diskon = 0
        potongan = 0
        total_bayar = total
        print("Tidak menggunakan kupon.")
    else:
      
        if kode in kupon:
            diskon = kupon[kode]
            potongan = total * (diskon / 100)
            total_bayar = total - potongan

            print(f"Kupon valid! Diskon {diskon}% diterapkan.")
            del kupon[kode]  
        else:
            print("Kupon tidak valid atau sudah digunakan! Tidak ada diskon.")
            diskon = 0
            potongan = 0
            total_bayar = total

   
    while True:
        try:
            bayar = float(input("Masukkan jumlah uang bayar: "))
            if bayar < total_bayar:
                print("Uang tidak cukup! Masukkan jumlah yang lebih besar.")
                continue
            break
        except ValueError:
            print("Input harus berupa angka.")

    kembalian = bayar - total_bayar

    print("===== STRUK BELANJA =====")
    print(f"Total Belanja : Rp {total}")
    print(f"Diskon        : {diskon}%")
    print(f"Potongan      : Rp {potongan}")
    print(f"Total Bayar   : Rp {total_bayar}")
    print(f"Uang Bayar    : Rp {bayar}")
    print(f"Kembalian     : Rp {kembalian}")
    print("==========================")

while True:
    print("=== MENU KUPON DISKON ===")
    print("1. Tampilkan semua kupon")
    print("2. Proses transaksi")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_kupon()
    elif pilih == "2":
        proses_transaksi()
    elif pilih == "3":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid.")

