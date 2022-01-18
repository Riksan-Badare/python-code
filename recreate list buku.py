anak_telkom = ['Iksan','Ikbal','Rudi','Dedox']
print(anak_telkom)

print('\nMenampilkan nama anak telkom dengan for in range')
for i in range (0, len(anak_telkom)):
    print(anak_telkom[i])

print('\nMenampilkan anak telkom Ikbal dan Dedos')
print(anak_telkom[1],anak_telkom[3])

print('\nMenampilkan isi variabel anak telkom')
for telkom in anak_telkom:
    print(telkom)