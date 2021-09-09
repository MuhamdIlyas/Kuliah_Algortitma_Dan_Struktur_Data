print "--------------------------------------------------"
print "           Contoh fungsi - parameter 2            "
print "--------------------------------------------------"
print  " "

def cetak_minimal(a, b):
    if a < b:
        print "merupakan nilai minimal", a
    elif a==b:
        print "sama dengan", (a, b)
    else :
        print "merupakan nilai minimal", b

print " "

while True:
    a = raw_input ("Masukkan nilai a :")
    b = raw_input ("Masukkan nilai b :")
    if a == "stop":
        break
    cetak_minimal(a, b)
    print " "

print "selesai"
