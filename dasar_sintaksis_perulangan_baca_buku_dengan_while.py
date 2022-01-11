"""
program perulangan membaca buku dengan while
"""
jumlah_buku = 15
print('Ibu berkata,"Bacalah semua buku ini"')

jumlah_buku_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_dibaca} buku")

while jumlah_buku_dibaca < jumlah_buku:
    jumlah_buku_dibaca = jumlah_buku_dibaca + 1
    print(f"Baca buku yang ke {jumlah_buku_dibaca}")


print(f"jumlah buku yang sudah dibaca {jumlah_buku_dibaca}")