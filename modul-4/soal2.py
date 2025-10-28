total_gaji = 0
total_jam_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")

    jam = int(input("Masukkan jam lembur: "))
    
    if 1 <= jam <= 3:
        gaji_lembur = jam * 25000
    elif jam == 4:
        gaji_lembur = 100000
    elif jam == 6:
        gaji_lembur = 200000
    elif jam == 8:
        gaji_lembur = 300000
    elif jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 0
        jam = 0
    else:
        gaji_lembur = 0
shift = input("Apakah shift malam? (y/n): ")

if shift == "y" or shift == "Y":
        bonus = 50000
else:
        bonus = 0

gaji_harian = 100000 + gaji_lembur + bonus

total_gaji += gaji_harian
total_jam_lembur += jam
total_bonus += bonus

print("--- Rekap Gaji Mingguan Pak Wowo ---")
print("Total jam lembur:", total_jam_lembur, "jam")
print("Total bonus shift malam: Rp", total_bonus)
print("Total gaji seminggu: Rp",total_gaji)        