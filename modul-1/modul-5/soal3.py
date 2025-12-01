def hitung_gaji_bersih(nama, jabatan, gaji_pokok):

    if jabatan == "Manager" or jabatan == "manager":
        persen_tunjangan = 0.10
    elif jabatan == "Staff" or jabatan == "staff":
        persen_tunjangan = 0.05
    else:
        persen_tunjangan = 0.00   

    pph = 0.05 * gaji_pokok
    tunjangan = persen_tunjangan * gaji_pokok
    gaji_bersih = gaji_pokok - pph + tunjangan

    print("===== RINCIAN GAJI =====")
    print("Nama            :", nama)
    print("Jabatan         :", jabatan)
    print("Gaji Pokok      : Rp", gaji_pokok)
    print("PPh (5%)        : Rp", pph)
    print("Tunjangan       : Rp", tunjangan)
    print("------------------------------")
    print("Gaji Bersih     : Rp", gaji_bersih)
    print("==============================")

    return gaji_bersih

print("=== Program Perhitungan Gaji Bersih Bulanan ===")

nama = input("Masukkan nama karyawan : ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")

while True:
    try:
        gaji_pokok = float(input("Masukkan gaji pokok: "))
        if gaji_pokok < 0:
            print("Gaji pokok tidak boleh negatif!") #dibuat perulangan
        else:
            hitung_gaji_bersih(nama, jabatan, gaji_pokok)
    except ValueError:
        print("Input gaji harus berupa angka!")
