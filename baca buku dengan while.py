jumlah_buku = 15
buku_dibaca = 0

print('Ibu berkata "Budi bacalah semua buku ini"')
print(f"Jumlah buku yang harus dibaca {jumlah_buku} buku")

print('Budi berkata "Baik Ibu"')
while jumlah_buku > buku_dibaca:
    buku_dibaca = buku_dibaca + 1
    print(f"Budi membaca buku ke {buku_dibaca}")

print(f"Jumlah buku yang telah dibaca Budi sebanyak {buku_dibaca} buku")
