"""
Program perulangan membaca buku dengan while sampai paham
"""

jumlah_buku = 14
jumlah_buku_yang_dibaca_dan_dipahami = 0
total_jumlah_baca = 0

print('Ibu berkata, "Budi baca dan pahami semua buku ini"')
print(f"Jumlah buku yang harus dibaca {jumlah_buku}")

print('Budi berkata,"Baik ibu saya akan membaca semua buku ini"')

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_dibaca_dan_dipahami == 13 :
        print(f"Budi sudah membaca ke {jumlah_buku_yang_dibaca_dan_dipahami + 1} dan tidak paham")
    else:
        jumlah_buku_yang_dibaca_dan_dipahami = jumlah_buku_yang_dibaca_dan_dipahami + 1
        print(f"Budi sudah membaca dan memahami buku ke {jumlah_buku_yang_dibaca_dan_dipahami}")

print(f"Budi telah membaca dan memahami buku sebanyak {jumlah_buku_yang_dibaca_dan_dipahami} buku")

if jumlah_buku_yang_dibaca_dan_dipahami == jumlah_buku:
    print('Budi berkata "Bu, saya sudah selesai dan memahami semua buku ini"')
else:
    print('Budi berkta,"Bu, tidak semua buku dapat saya pahami"')



