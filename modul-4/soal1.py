baris_total = int(input("Masukkan jumlah baris lampu: "))

for baris in range(1, baris_total + 1):
    lampu_total = int(input(f"Masukkan jumlah lampu di baris {baris}: "))

    for lampu in range(1, lampu_total + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
    
    if baris == baris_total:
        print("Periksa sambungan daya utama.")