#Latihan Tuple
print "-----------------------------------------------------------------"
print "                           Latihan Tuple                         "
print "-----------------------------------------------------------------"
print " "
A = ("Program", "Studi", "Teknik", "Informatika")
print "Nilai elemen tuple A dengan Indeks ke 0 adalah", A[0]
print " "

#latihan Tuple 1
print "-----------------------------------------------------------------"
print "                           Latihan Tuple                         "
print "-----------------------------------------------------------------"
print " "
print "Variabel Tuple: "
print "A = (Program, Studi, Teknik, Informatika, UNISNU, Jepara)"
print "B = 10, 20, 30, 40, 50, 60, 70"
print " "
print "Tampilkan :"
A = ("Program", "Studi", "Teknik", "Informatika", "UNISNU", "Jepara")
B = 10, 20, 30, 40, 50, 60, 70
print "Nilai elemen tuple A dengan Indeks ke 0 dan 3 adalah", A[0],A[3]
print "Nilai elemen tuple B dengan Indeks ke 2 sampai dengan 5 adalah", B[2:6]
print " "

#latihan Tuple 2
print "-----------------------------------------------------------------"
print "                           Latihan Tuple                         "
print "-----------------------------------------------------------------"
print " "
print "Variabel Tuple: "
print "A = (Program, Studi, Teknik, Informatika, UNISNU, Jepara)"
print "B = 10, 20, 30, 40, 50, 60, 70"
print " "
print "Tampilkan :"
A = ("Program", "Studi", "Teknik", "Informatika", "UNISNU", "Jepara")
B = 10, 20, 30, 40, 50, 60, 70
input1 = raw_input ("Masukkan inputan nilai elemen tuple A yang ingin di di tampilkan :")
input2 = raw_input ("Masukkan inputan nilai elemen Tuple B yang ingin di tampilkan dari indeks ke :")
input3 = raw_input ("Sampai dengan indeks ke :")
print " "
print "Hasilnya adalah :" 
print "Nilai elemen tuple A yang ingin ditampilkan adalah", A[int(input1)]
print "Nilai elemen tuple B yang ingin ditampilkan adalah", B[int(input2):int(input3)]
