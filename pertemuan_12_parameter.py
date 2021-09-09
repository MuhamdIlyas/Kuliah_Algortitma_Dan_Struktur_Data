#contoh fingsi -  function
print "--------------------------------------------------"
print "             Contoh fungsi - parameter            "
print "--------------------------------------------------"

def judul(prodi):
    print "program studi",prodi

def cetak_maksimal(a,b):
    if a > b:
        print "%s merupakan nilai maksimal" % a
    elif a==b:
        print "%s sama dengan %s" % (a,b)
    else :
        print"%s merupakan nilai maksimal" % b

#memanggil fungsi judul dengan argumen "teknik informatika"
judul("teknik informatika")

print " "

#memanggil fungsi judul dengan argumen "budidaya perairan"
judul("budidaya perairan")

print " "

cetak_maksimal (10, 100)
cetak_maksimal (1, 9)
cetak_maksimal (100, 800)
cetak_maksimal (10, 90)
cetak_maksimal (1000, 2345)
