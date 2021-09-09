#latihan modul math
print "------------------------------------------------------"
print "                   Contoh Modul Math                  "
print "------------------------------------------------------"
print " "

import math
#konstanta
print 'Nilai Konstanta'
print 'pi = ', math.pi
print 'e  = ', math.e
print " "

#faktorial, n!
print 'Nilai Faktorial, n!'
for i in range(1,11) :
    print '%s! = %s' %(i, math.factorial(i))
print " "

#pangkat
print 'Contoh Nilai Pangkat '
print ' 2 pangkat 12 =', math.pow(2, 12)
print " "

#akar kuadrat
print 'Contoh Nilai Akar Kuadrat '
print 'Akar Kuadrat 10 =', math.sqrt(10)
print " "

#logaritma
print 'COntoh Nilai Logaritma '
print 'log 8          =', math.log(8)
print 'log 8 basis 10 =', math.log(8, 10)
print 'log 8 basis 10 =', math.log10(8)
print " "

#trigonometri
print 'Contoh Nilai Trigonometri '
print 'sin 90 derajat =', math.sin(math.radians(90))
print 'sin 45 derajat =', math.sin(math.radians(45))
print 'sin 30 derajat =', math.sin(math.radians(30))
print " "
