# t1 = (3, 1, 4)
# t2 = (1, 5, 9)

# duatuple = t1 + t2
# print("Hasil penggabungan:", duatuple)

# tanpa_duplikat = []
# for angka in duatuple:
#     if angka not in tanpa_duplikat:
#         tanpa_duplikat.append(angka)
# print("Setelah hapus duplikat:", tanpa_duplikat)

# urut_menurun = []
# while tanpa_duplikat:
#     terbesar = max(tanpa_duplikat)      
#     urut_menurun.append(terbesar)       
#     tanpa_duplikat.remove(terbesar)     
# print("Setelah diurutkan menurun:", urut_menurun)

 # t1 t2 minta inputan

t1_input = input("Masukkan elemen tuple pertama (pisahkan dengan spasi): ").split()
t1 = tuple(int(angka) for angka in t1_input)  

t2_input = input("Masukkan elemen tuple kedua (pisahkan dengan spasi): ").split()
t2 = tuple(int(angka) for angka in t2_input)

duatuple = t1 + t2
print("Hasil penggabungan:", duatuple)

tanpa_duplikat = []
for angka in duatuple:
    if angka not in tanpa_duplikat:
        tanpa_duplikat.append(angka)
print("Setelah hapus duplikat:", tanpa_duplikat)

urut_menurun = []
while tanpa_duplikat:
    terbesar = max(tanpa_duplikat)
    urut_menurun.append(terbesar)
    tanpa_duplikat.remove(terbesar)

print("Setelah diurutkan menurun:", urut_menurun)

 