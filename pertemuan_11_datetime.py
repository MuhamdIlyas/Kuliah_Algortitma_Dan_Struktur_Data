#latihan library standard
print "------------------------------------------------------"
print "                 Contoh Modul Datetime                "
print "------------------------------------------------------"
print " "

import datetime
import time
sekarang = datetime.datetime.now()
tanggal = sekarang.date()
waktu = sekarang.time()


print 'Hari Ini Adalah :'
print 'Tanggal  :', tanggal.day
print 'Bulan    :', tanggal.month
print 'Tahun    :', tanggal.year
print 'Tanggal / Bulan / Tahun  :',tanggal.day,'/',tanggal.month,'/',tanggal.year
print " "

print 'Tanggal  :', datetime.datetime.now().date()
print 'Waktu    :', datetime.datetime.now().time()
print " "

print 'Tanggal  :', tanggal
print 'Waktu    :', waktu
print " "

print 'Jam  :', waktu.hour
print 'Menit:', waktu.minute
print 'Detik:', waktu.second

time.sleep(5)

sekarang2 = datetime.datetime.now()
delta = sekarang2 - sekarang

print " "
print 'Selisih Detik :', delta.total_seconds()

print " "
