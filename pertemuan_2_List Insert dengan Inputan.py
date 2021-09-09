# pertemuan 2, List Insert dengan Ipnutan
print " "
print "====================================================================="
print "===================== List Insert dengan Inputan ===================="
print "====================================================================="
print " "
print "Ini adalah List a : [0,1,2,3,4]"
print " "
a = [0,1,2,3,4]
index = raw_input ("Masukkan Index yang akan di Insert :")
obj = raw_input   ("Masukkan Objek yang akan di Insert :")
a.insert (int(index),obj)
print " "
print "Hasil List a setelah di Insert :",a

print " "
print "====================================================================="
print "================= Latihan List Insert dengan Inputan ================"
print "====================================================================="
print " "

print "Nama   : Mochammad, Haji"
print "Alamat : Jl, Taman, Pekeng, Tahunan, Jepara"
a = ["Mochammad", "Haji"]
index = raw_input ("Masukkan Index yang akan di Insert :")
obj = raw_input   ("Masukkan Objek yang akan di Insert :")
a.insert (int(index),obj)
print " "
b = ["Jl", "Taman", "Pekeng", "Tahunan", "Jepara"]
index = raw_input ("Masukkan Index yang akan di Insert :")
obj = raw_input   ("Masukkan Objek yang akan di Insert :")
b.insert (int(index),obj)
print " "
print "Nama setelah di Insert  :", a
print "Alamat setelah di Insert:", b
