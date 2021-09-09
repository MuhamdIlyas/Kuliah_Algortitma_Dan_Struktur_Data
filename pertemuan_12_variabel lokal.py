#contoh fingsi -  function
print "--------------------------------------------------"
print "          Contoh fungsi - Variabel Lokal          "
print "--------------------------------------------------"
print " "

x = 50
def fungsi(x):
    print "x =", x
    x = 2
    print "merubah lokal variabel x =", x

fungsi(100)
print "nilai x masih tetap =", x
