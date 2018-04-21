import texttable as tt
import getpass
import math


def menu():
    print("=====================================")
    print("\n\t---pilihan---")
    print("\t1. pembayaran mahasiswa")
    print("\t2. penilain mahasiswa")
    print("\t3. kalkulator sederhana")

    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1":
        pembayaran()
    elif pilih == "2":
        nilai_mahasiswa()
    elif pilih == "3":
        kalkulator()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input................!!!")

def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []

    x = [[]]

    jawab = "y"

    tab = tt.Texttable()

    while (jawab == 'y'):
        print("\n======================================")
        nama.append(input("\n\tMasukan Nama: "))
        nim.append(input("\tMasukan Nim: "))
        tugas = int(input("\tNilai Tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("\tNilai UTS: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("\tNilai UAS: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("\n\tTambah data [y/n]? ")

    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['l','l','l','r','r','r','r'])
    tab.header(['No','Nama','Nim','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Akhir'])
    print (tab.draw())

def pembayaran():
    print("\n=============================================")
    nama = input("\n\tmasukan nama = ")
    nim = input("\tmasukan nim = ")
    semester = input("\tmasukan semester saat ini = ")
    print("\n\t---pilihan pembayaran---")
    print("\t1. pembayaran spp")
    print("\t2. pembayaran uts")
    print("\t3. pembayaran uas")
    print("\t4. pembayaran spp & uts")
    print("\t5. pembayaran spp & uas")
    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1":
        spp()
    elif pilih == "2":
        uts()
    elif pilih == "3":
        uas()
    elif pilih == "4":
        spp_uts()
    elif pilih == "5":
        spp_uas()
    else:
        exit
        tanya()
        
def spp():
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 500000*bulan
    print("==============================================================")
    print("\ttotal bayar spp Rp.500000 *" ,bulan," = Rp.",total)

def uas():
    matkul = int(input("\n\tjumlah mata kuliah = "))
    matkul = float(matkul)
    byr_uas = 50000*matkul
    print("=============================================================")
    print("\ttotal bayar uas Rp.50000 *",matkul," = Rp.",byr_uas)

def uts():
    matkul = int(input("\n\tjumlah mata kuliah = "))
    matkul = float(matkul_uts)
    byr_uts = 50000*matkul_uts
    print("=============================================================")
    print("\ttotal bayar uas Rp.50000 *",matkul," = Rp.",byr_uts)

def spp_uas():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    matkul =int(input("\tjumlah mata kuliah = "))
    matkul =float(matkul)
    bulan = float(bulan)
    total_spp = 500000 * bulan
    byr_uas = 50000*matkul
    total = total_spp + byr_uas + 5000
    print("\n\ttotal bayar spp Rp.500000 * ",bulan," = Rp.",total_spp)
    print("\ttotal bayar uas Rp.50000 * ",matkul," = Rp.",byr_uas)
    print("\tbiaya tambahan server sebesar RP.5000")
    print("============================================================")
    print("\ttotal yang harus di bayar Rp",total)

def spp_uts():
    bulan=int(input("\n\tjumlah bulan yang di bayar = "))
    matkul =int(input("\tjumlah mata kuliah = "))
    matkul =float(matkul)
    bulan = float(bulan)
    total_spp = 500000 * bulan
    byr_uts = 50000*matkul
    total = total_spp + byr_uts + 5000
    print("\n\ttotal bayar spp Rp.50000 * ",matkul," = Rp.",byr_uts)
    print("\ttotal bayar uas Rp.500000 * ",bulan," = Rp.",total_spp)
    print("\tbiaya tambahan server sebesar RP.5000")
    print("============================================================")
    print("\ttotal yang harus di bayar Rp",total)

def kalkulator():
    print('\n\t==================================')
    print('Program Kalkulator Sederhana')
    print('1. Pertambahan')
    print('2. Pengurangan')
    print('3. Pembagian')
    print('4. Perkalian')

    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1":
       tambah()
    elif pilih == "2":
         kurang()
    elif pilih == "3":
         bagi()
    elif pilih == "4":
         kali()
    else:
        exit
    tanya()
    
def tambah ():
    print('\t1, Pejumlahan')
    a = int(input('\tMasukan nilai Pertama= '))
    b = int(input('\tMasukan nilai Kedua= '))
    c = a+b
    print ('\tPertama+Kedua=',c)
    tanya ()
def kurang ():
    print('\t2, Pengurangan')
    a = int(input('\tMasukan nilai Pertama= '))
    b = int(input('\tMasukan nilai Kedua= '))
    c = a-b
    print ('\tPertama-Kedua=',c)
    tanya ()
def bagi ():
    print('\t3, Pembagian')
    a = int(input('\tMasukan nilai Pertama= '))
    b = int(input('\tMasukan nilai Kedua= '))
    c = a/b
    print ('\tPertama/Kedua=',c)
    tanya ()
def kali ():
    print('\t4, Pengkalian')
    a = int(input('\tMasukan nilai Pertama= '))
    b = int(input('\tMasukan nilai Kedua= '))
    c = a*b
    print ('\tPertama*Kedua=',c)
    tanya ()

def tanya ():
    tanya = input("\n\tKembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input...............!!!")

username = input("\nUsername : ")
password = getpass.getpass()
print("=========================================")

if username == "Satria" and password == "Zura112":
    menu()

else:
    print ("maaf password atau username mu salah............!!!")
    
    
