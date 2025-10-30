# total_gaji = 0
# total_jam_lembur = 0
# total_bonus = 0

# for hari in range(1, 8):
#     print(f"Hari ke-{hari}")

#     jam = int(input("Masukkan jam lembur: "))
    
#     if 1 <= jam <= 3:
#         gaji_lembur = jam * 25000
#     elif jam == 4:
#         gaji_lembur = 100000
#     elif jam == 5:
#          gaji_lembur = 150000    
#     elif jam == 6:
#         gaji_lembur = 200000
#     elif jam == 7:
#          gaji_lembur = 250000    
#     elif jam == 8:
#         gaji_lembur = 300000
#     elif jam > 8:
#         print("Lembur melebihi batas, hanya dihitung 8 jam")
#         gaji_lembur = 0
#         bonus = 0
        
#     else:
#         gaji_lembur = 0
# shift = input("Apakah shift malam? (y/n): ")

# if shift == "y" or shift == "Y":
#         bonus = 50000
# else:
#         bonus = 0

# gaji_harian = 100000 + gaji_lembur + bonus

# total_gaji += gaji_harian * 7 + total_jam_lembur + total_bonus
# total_jam_lembur += jam 
# gaji_lembur = 
# total_bonus += bonus

total_gaji = 0
total_jam_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")
    
    shift = input("Apakah hari ini shift malam? (y/n): ").lower()
    if shift == "y":
        bonus = 50000
        print("Bonus shift malam: Rp50.000")
    else:
        bonus = 0
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur hari ini: "))
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka bulat (integer).")

    if jam_lembur > 8:
        print("Lembur melebihi batas, hanya 8 jam yang dihitung.")
        jam_lembur = 8
    elif jam_lembur < 0:
        print("Jam lembur tidak boleh negatif, dianggap 0.")
        jam_lembur = 0

    if jam_lembur == 0:
        lembur = 0
    elif 1 <= jam_lembur <= 3:
        lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur = 100000
    elif jam_lembur == 5:
        lembur = 150000   
    elif jam_lembur == 6:
        lembur = 200000
    elif jam_lembur == 7:
        lembur = 250000    
    elif jam_lembur == 8:
        lembur = 300000
    else:
        lembur = 0    

    gaji_harian = 100000 + lembur + bonus

    total_gaji += gaji_harian
    total_jam_lembur += jam_lembur
    total_bonus += bonus

    print(f"Gaji hari ke-{hari}: Rp{gaji_harian:,}")


print("=== Rangkuman Gaji Mingguan ===")
print(f"Total jam lembur: {total_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")