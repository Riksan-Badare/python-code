"""
program perulangan membaca buku
"""
jumlah_buku = 20
jumlah_buku_yang_sudah_dibaca = 0

print('Ibu berkata,"Baca semua bukumu"')
print(f"jumlah buku yang belum dibaca {jumlah_buku}")

for jumlah_buku_yang_sudah_dibaca in range (1, jumlah_buku+1):
    print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca} sudah di baca")

print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca} buku")
if jumlah_buku_yang_sudah_dibaca==20:
    print('Anak berkata,"Ibu saya sudah selesai membaca buku"')
else:
    print('Anak berkata,"Saya belum membaca buku"')
