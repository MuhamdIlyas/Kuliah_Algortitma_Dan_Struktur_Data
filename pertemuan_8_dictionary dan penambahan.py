print "======================================================"
print "Latihan 1 Progam Python Menggunakan Inputan Dictionary"
print "======================================================"
print " "

nama = raw_input            ('Masukkan Nama         :')
alamat = raw_input          ('Masukkan Alamat Rumah :')
tempat_lahir = raw_input    ('Masukkan Tempat Lahir :')
tanggal_lahir = raw_input   ('Masukkan Tanggal Lahir:')
program_studi = raw_input   ('Masukkan Program Studi:')
nim = raw_input             ('Masukkan NIM          :')

biodata_mahasiswa = {'Nama':nama,'Alamat':alamat,'Tempat Lahir':tempat_lahir,'Tanggal Lahir':tanggal_lahir,'Program Studi':program_studi,'NIM':nim}

print " "
print " "
print "Cetak :"
print " "

print "Nama             :",biodata_mahasiswa['Nama']
print "Alamat           :",biodata_mahasiswa['Alamat']
print "Tempat Lahir     :",biodata_mahasiswa['Tempat Lahir']
print "Tanggal Lahir    :",biodata_mahasiswa['Tanggal Lahir']
print "Program Studi    :",biodata_mahasiswa['Program Studi']
print "NIM              :",biodata_mahasiswa['NIM']


print ' '
print ' '
print 'Contoh Menambah Dictionary'
print ' '
hobi = raw_input            ('Masukkan Hobi         :')
biodata_mahasiswa['Hobi']=hobi

print " "
print "Cetak :"
print "Nama             :",biodata_mahasiswa['Nama']
print "Alamat           :",biodata_mahasiswa['Alamat']
print "Tempat Lahir     :",biodata_mahasiswa['Tempat Lahir']
print "Tanggal Lahir    :",biodata_mahasiswa['Tanggal Lahir']
print "Program Studi    :",biodata_mahasiswa['Program Studi']
print "NIM              :",biodata_mahasiswa['NIM']
print "Hobi             :",biodata_mahasiswa['Hobi']
print ' '

print ' '
print ' '
print 'Contoh Menambah Dictionary'
print ' '
nama = raw_input            ('Masukkan Nama Baru         :')
biodata_mahasiswa['Nama']=nama

print " "
print "Cetak :"
print "Nama             :",biodata_mahasiswa['Nama']
print "Alamat           :",biodata_mahasiswa['Alamat']
print "Tempat Lahir     :",biodata_mahasiswa['Tempat Lahir']
print "Tanggal Lahir    :",biodata_mahasiswa['Tanggal Lahir']
print "Program Studi    :",biodata_mahasiswa['Program Studi']
print "NIM              :",biodata_mahasiswa['NIM']
print "Hobi             :",biodata_mahasiswa['Hobi']
print ' '

print ' '
print ' '
print 'Contoh Menghapus Dictionary(menghapus item berdasarkan kata kunci)'
print ' '
del biodata_mahasiswa['Hobi'];
print ' '
print biodata_mahasiswa

print ' '
print ' '
print 'Contoh Menghapus Dictionary(semua item)'
print ' '
biodata_mahasiswa.clear();
print ' '
print biodata_mahasiswa
