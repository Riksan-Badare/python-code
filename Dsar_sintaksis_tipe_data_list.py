daftar_buku = ['Seven Habits','How to Influence People','First Things First', '4DX']
print('\nTampilkan Variabel daftar_buku')
print(daftar_buku)

for buku in daftar_buku:
    print(buku)

print('\nProses semua dengan for in')
print(daftar_buku[0])

print('\nTampilkan daftar buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
print('\nTampilkan dengan for in range dimana tipe data tiap elemen berbeda-beda')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Seven Habits','How to Influence People','First Things First', '4DX']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Lovasket')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMenghapus list')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMengubah isi pertama dalam suatu list/array')
daftar_buku = ['Seven Habits','How to Influence People','First Things First', '4DX']
daftar_buku[0] = 'The Witcher'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke dua')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop, diambil tanpa variabel jadi isi list terakhir yang diambil')
daftar_buku = ['Seven Habits','How to Influence People','First Things First', '4DX']
daftar_buku.pop(-1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])