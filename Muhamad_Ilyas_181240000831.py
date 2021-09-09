#Jadwal Mengajar Guru
import datetime
import time
now=datetime.datetime.now()
tanggal=now.date()
waktu=now.time()

kop='''
=====================================================================================================
*********************************|     MI Negeri 01 Karanggondang    |******************************
**************|     E-mail: MtsN01krg@gmail.com, Phone:082120349454, Kode pos: 59452    |************
***************************|  Jalan Kenanga Nomer 17 Karanggondang Mlonggo  |************************
=====================================================================================================
'''

def menu ():
    print"                            <:: MENU ::>"
    print"                     ============================"
    print"                            1. Mengajar"
    print"                            2. Tugas"
    print"                            3. Keluar"
    print ' '
    pilih=raw_input ("\t\t\t Masukkan Pilihan :")
    if pilih=="1":
        mengajar()
    elif pilih=="2":
        tugas()
    elif pilih=="3":
        keluar()
    else:
        print""

def mengajar():
    print''
    print'       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    print'       ============= Jadwal Mengajar Guru =============='
    print'       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    print ' '
    
    kode=raw_input("\tMasukkan Kode Guru        : ")
    nama=raw_input("\tMasukkan Nama             : ")
    mapel=raw_input("\tMasukkan Mata Pelajaran   : ")
    hari=raw_input("\tMasukkan Hari             : ")

    data_guru = {'Kode':kode,'Nama':nama,'Mapel':mapel,'Hari':hari}
    data_jam = {'IPS':'07.00-08.00','IPA':'08.00-09.00','MTK':'09.30-10.30','BTA':'10.30-11.30'}
    
    print ' '
    print '\t\tCetak :'
    print ' '

    print '\tKode Guru        :',data_guru['Kode']
    print '\tNama             :',data_guru['Nama']
    print '\tMata Pelajaran   :',data_guru['Mapel']
    print '\tHari             :',data_guru['Hari']
    print '\tJam Mengajar     :',data_jam[mapel]
    print ' '

    print '\tDicetak Pada :'
    print ' '
    print '\tTanggal  :', tanggal
    print '\tWaktu    :', waktu
    print ' '
    
    print '\t\t====SEMANGAT,, GOOD LUCK !!===='
    print '\t====SEMOGA ILMU YANG ANDA SAMPAIKAN BERMANFAAT===='
    print ' '
    
    while True:
        tanya=raw_input("\t =====Yakin Meninggalkan Jadwal Ini ?(Y/T)")
        print ' '
        if tanya=="t":
            tugas()
        elif tanya=="y":
            menu()
            break
        elif not tanya:
            print
        else:
            print
        print ' '

def tugas():
    print''
    print'        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    print'        ================== Input Tugas =================='
    print'        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    print ' '
    kode=raw_input("\tMasukkan Kode Guru        : ")
    nama=raw_input("\tMasukkan Nama             : ")
    hari=raw_input("\tMasukkan Hari             : ")
    kelas=raw_input("\tMasukkan Kelas            : ")
    mapel=raw_input("\tMasukkan Mata Pelajaran   : ")
    tugas=raw_input("\tMasukkan Tugas            : ")

    
    data_guru = {'Kode':kode,'Kelas':kelas,'Nama':nama,'Mapel':mapel,'Hari':hari,'Tugas':tugas}
    data_jam = {'IPS':'07.00-08.00','IPA':'08.00-09.00','MTK':'09.30-10.30','BTA':'10.30-11.30'}
    
    
    print ' '
    print ' '
    print '\t\tCetak :'
    print ' '

    print '\tKode Guru        :',data_guru['Kode']
    print '\tNama             :',data_guru['Nama']
    print '\tHari             :',data_guru['Hari']
    print '\tKelas            :',data_guru['Kelas']
    print '\tMata Pelajaran   :',data_guru['Mapel']
    print '\tJam Mengajar     :',data_jam[mapel]
    print '\tTugas            :',data_guru['Tugas']
    print ' '

    print '\tDicetak Pada :'
    print ' '
    print '\tTanggal  :', tanggal
    print '\tWaktu    :', waktu
    print ' '
    
    print '\t\t======= SELAMAT MENGERJAKAN ======='
    print '\t\t====== KERJAKAN SEBAIK-BAIKNYA ====='
    print ' '
    
    while True :
        tanya = raw_input ("\t Tambah Tugas ?(Y/T) :")
        print ' '
        if tanya == "Y" or tanya == "y":
            print ' '
            tambah()
        elif tanya == "T" or tanya == "t" :
            menu()
            break
        elif not tanya:
            print ' '
        else:
            print ' '

def tambah():
    print''
    print'        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    print'        ================= Tugas Tambahan ================'
    print'        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    print ' '
    kode=raw_input("\tMasukkan Kode Guru        : ")
    nama=raw_input("\tMasukkan Nama             : ")
    kelas=raw_input("\tMasukkan Kelas            : ")
    mapel=raw_input("\tMasukkan Mata Pelajaran   : ")
    tugas=raw_input("\tMasukkan Tugas Tambahan   : ")
    
    data_guru = {'Kode':kode,'Kelas':kelas,'Nama':nama,'Mapel':mapel,'Tugas':tugas}
    data_jam = {'IPS':'07.00-08.00','IPA':'08.00-09.00','MTK':'09.30-10.30','BTA':'10.30-11.30'}
    
    
    print ' '
    print ' '
    print '\t\tCetak :'
    print ' '

    print '\tKode Guru        :',data_guru['Kode']
    print '\tNama             :',data_guru['Nama']
    print '\tKelas            :',data_guru['Kelas']
    print '\tMata Pelajaran   :',data_guru['Mapel']
    print '\tJam Mengajar     :',data_jam[mapel]
    print '\tTugas Tambahan   :',data_guru['Tugas']
    print ' '

    print '\tDicetak Pada :'
    print ' '
    print '\tTanggal  :', tanggal
    print '\tWaktu    :', waktu
    print ' '
    
    print '\t======= JANGAN PERNAH LELAH DALAM BELAJAR ======='
    print ' '

def keluar():
    print ' '
    print '\t====TERIMA KASIH TELAH MENGGUNAKAN APLIKASI INI===='
    print '\t\t====MARI KITA MERAWATNYA BERSAMA===='
    print ' '
    print kop
    print ' '

print kop
def login():
    print ''
    print''
    print'                            <:: LOG IN ::>'
    print'                     ============================='
    print' '
    print ' '
    
while True:
    user=raw_input("\t\t\t     Username : ")
    pas=raw_input("\t\t\t     Password : ")
    if pas == "sekolah" and user =="sekolah":
        print ''
        menu ()
    else:
        print "\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        print "\t= Maaf Username atau Password yang anda Masukkan Tidak Sesuai="
        print "\t==================== Silahkan COba Lagi ======================"
        print "\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        login ()

login()

