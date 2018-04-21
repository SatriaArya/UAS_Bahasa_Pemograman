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
    tanya ()def bagi ():
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
    tanya = input("\n\tKembali ke menu kalkulator (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input...............!!!")