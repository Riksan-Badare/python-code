"""
program perulangan membaca buku
"""
jumlah_buku = 10
jumlah_buku_yang_sudah_dibaca = 0

print('Ibu berkata, "baca semua bukumu"')
print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")

for jumlah_buku_yang_sudah_dibaca in range (1, jumlah_buku+1):
    print (f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print (f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")
