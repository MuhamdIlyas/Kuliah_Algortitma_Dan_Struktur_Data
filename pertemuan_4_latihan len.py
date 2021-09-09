print "---------------------------------------------------------------------------------"
print " Program Menghitung Jumlah Mahasiswa di dalam Suatu Kelas menggunakan Fungsi LEN "
print "---------------------------------------------------------------------------------"
print " "

print "Kelas A = [PRASETYO, RIFQI, ARIF, WULAN, GERAL, NISA, LITA, AJI, BAMBANG, ABTHOL, LUTFY,YONGKY]"
print "Kelas B = [YOGA, IQBAL, MIRMANTO, CHACHA, IRWAN, ALFIANTO]"
print "Kelas C = [AFIFI, DODI, ANGGARA, FIKIH, RESTU, SUFYAN, BAMBANG, VITA, VIKI, MEIRINA]"
A =["PRASETYO", "RIFQI", "ARIF", "WULAN", "GERAL", "NISA", "LITA", "AJI", "BAMBANG", "ABTHOL", "LUTFY","YONGKY"]
B =["YOGA", "IQBAL", "MIRMANTO", "CHACHA", "IRWAN", "ALFIANTO"]
C =["AFIFI", "DODI", "ANGGARA", "FIKIH", "RESTU", "SUFYAN", "BAMBANG", "VITA", "VIKI", "MEIRINA"]
while True :
    input = raw_input ("Masukkan nama kelas yang akan dihitung jumlah mahasiswanya pada kelas :")
    if input =="A":
        input=A
    else:
        if input=="B":
            input=B
        else:
            if input=="C":
                input=C
            else:
                if input=="stop":
                       break
    print "------------------------->Jumlah mahasiswa pada kelas tersebut adalah :", len(input)
    print " "

print " "
print "SELESAI"
