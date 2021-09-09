print " "
print "====================================================================="
print "============= List remove dengan Inputan dan Perulangan ============="
print "====================================================================="
print " "
print "Ini adalah List a : [TIF, TI, TS, TE, SI, DP, DKV, Budidaya Perairan]"
print " "
a = ["TIF", "TI", "TS", "TE", "SI", "DP", "DKV", "Budidaya Perairan"]
while True :
    objek = raw_input ("Masukkan Objek yang akan dihapus :")
    if objek =="stop" :
        break
    a.remove(str(objek))
    print " "
    print "Hasil list setelah a di edit :",a
print "Selesai"
