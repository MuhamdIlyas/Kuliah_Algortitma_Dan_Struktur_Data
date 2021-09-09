# Latihan List Delete dengan Inputan dan Perulangan
print " "
print "====================================================================="
print "============= List delete dengan Inputan dan Perulangan ============="
print "====================================================================="
print " "
print "Ini adalah List a : [10,7,21,19,32,43,54]"
print " "
a = [10,7,21,19,32,43,54]
while True :
    objek = raw_input ("Masukkan Objek yang akan dihapus :")
    if objek =="stop" :
        break
    del a[int(objek)]
    print " "
    print "Hasil list setelah a di edit :",a
print "Selesai"
print " "
print "====================================================================="
print "============= List remove dengan Inputan dan Perulangan ============="
print "====================================================================="
print " "
print "Ini adalah List a : [10,7,21,19,32,43,54]"
print " "
a = [10,7,21,19,32,43,54]
while True :
    objek = raw_input ("Masukkan Objek yang akan dihapus :")
    if objek =="stop" :
        break
    a.remove(int(objek))
    print " "
    print "Hasil list setelah a di edit :",a
print "Selesai"
