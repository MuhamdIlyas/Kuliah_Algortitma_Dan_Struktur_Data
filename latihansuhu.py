print ""
print "************************************************************"
print "************* Program Suhu di Dalam Ruangan ****************"
print "************************************************************"
print ""

ruangan = raw_input ("\tMasukkan Nama Ruangan : ")
suhu    = int(input ("\tMasukkan Suhu Ruangan : "))
print ""
print "\tCetak"
print "\tNama Ruangan          :",ruangan
if (suhu <=20 ):
    print "\tKeterangan            : Suhu Ruangan Dingin",ruangan
else:
    print "\tKeterangan            : Suhu Ruangan Panas",suhu
    
print""
print "************************************************************"
print "************************************************************"
print "************************************************************"
print ""
