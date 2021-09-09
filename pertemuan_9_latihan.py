print "======================================================"
print "             Latihan Metode Dictionary                "
print "======================================================"
print " "

merk = raw_input            ('Masukkan Merk Motor Anda         :')
tipe = raw_input            ('Masukkan Type Motor Anda         :')
warna = raw_input           ('Masukkan Warna Motor Anda        :')
kecepatan = raw_input       ('Masukkan Kecepatan Motor         :')
tahun = raw_input           ('Masukkan Tahun Pembelian Motor   :')
print " "
print " "
while True :
    print "Macam-macam Pilihan Program :"
    print "1. Program Method Copy"
    print "2. Program Method Fromkey"
    print "3. Program Methode Value"
    print " "
    tanya = raw_input("Masukkan Pilihan Program :")
    if tanya == "stop":
        break
    elif tanya == "1":
        data = ("Merk":merk, "Type":tipe, "Warna":warna, "Kecepatan":kecepatan, "Tahun":tahun)
        dataCopy = data.copy()
        print "data Setelah di copy

print " "
