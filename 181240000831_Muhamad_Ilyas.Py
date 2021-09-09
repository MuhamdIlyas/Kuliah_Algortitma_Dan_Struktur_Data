# Nama  : Muhamad Ilyas
# NIM   : 181240000831
# Kelas : DC
# Prodi : Teknik Informatika / Pemrograman Terstruktur

# Latihan 1
# ----------------------> Perulangan FOR <----------------------------------
print"----------------------> Perulangan FOR <----------------------------------"

masakan_khas =["Horog-Horog","Pindang Srani","Pecel","Cendol","Pleret","Kintelan"]

for x in masakan_khas:
     print x, "adalah masakan khas dari daerah Jepara"


print ""


# Latihan 2
# ----------------------> Perulangan FOR <----------------------------------
print"----------------------> Perulangan FOR <----------------------------------"

nama  = ["Udin","Anas","Virgi","Faisal"]
lahir = ["Ngabul","Sinanggul","Kuwasen","Keling"]
hobi  = ["Vektor","Olahraga","Ngoding","Membaca"]
usia  = [21, 22, 23, 24]

for x in range(len(nama)):
     print "Nama saya adalah ",nama[x], "\nSaya berusia ",usia[x],"\nSaya lahir di ",lahir[x],"\nHobby saya adalah ",hobi[x]


print ""


# Latihan
# ----------------------> Perulangan FOR <----------------------------------
print "----------------------> Perulangan FOR <----------------------------------"

kelas = [1,3,5,7,9]

for x in range(len(kelas)):
     print "Nilai rata-rata nilai kelas ",kelas[x],"adalah : 85"


print ""


# Latihan 1              --> Program Pencetakan 1 <--
# ---------

x = int(raw_input("Masukkan berapa kali perulangan : "))

for i in range(x):
    print "Teknik Informatika UNISNU JEPARA"


print ""


# Latihan 2             --> Program Pencetakan 2 <--
# ---------

kalimat = raw_input("Masukkan kalimat yang ingin di cetak\t: ")
cetak   = raw_input("Masukkan berapa kali pencetakan\t\t: ")

for i in range(int(cetak)):
    print kalimat
        

print ""


# Latihan 3          --> Program Inputan Pencetakan <--
# ----------

nama   = raw_input("Masukkan Nama\t\t\t\t: ")
alamat = raw_input("Masukkan Alamat\t\t\t\t: ")
agama  = raw_input("Masukkan Agama\t\t\t\t: ")

print ""

cetak_nama   = raw_input("Masukkan berapa kali pencetakan Nama\t: ")
cetak_alamat = raw_input("Masukkan berapa kali pencetakan Alamat\t: ")
cetak_agama  = raw_input("Masukkan berapa kali pencetakan Agama\t: ")
print ""
for i in range(int(cetak_nama)):
    print nama
print ""

for i in range(int(cetak_alamat)):
    print alamat
print ""

for i in range(int(cetak_agama)):
    print agama
print ""
