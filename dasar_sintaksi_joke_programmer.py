"""
semua sintaksis pemrograman terdiri dari:
1.sekuensial
2.percabangan
3.perulangan
"""

# sequensial
print ('Ibu berkata, "pergi ke toko"')
print ('Budi menjawab, "baik apa yang harus saya lakukan?"')
print ('ibu berkata,"Beli satu botol susu, dan jika ada telor beli 6"')
print ("maka Budi berangkat ke toko")
print ("dan mulai berbelanja")

# percabangan
jumlah_botol_susu=200
jumlah_telur=4342

print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya")
    print("Budi membeli 1 botol susu")
else:
    print("Budi tidak membeli susu")
if jumlah_telur > 0:
    print("Budi membeli 6 telur")
else:
    print("Budi tidak membeli telur")
print("Budi pulang ke rumah")
print("Budi menyampaikan hasilnya kepada Ibu")

