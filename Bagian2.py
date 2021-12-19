def persegipanjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar

    print('Keliling:', keliling,'\nLuas:', luas)

def segitiga(alas, tinggi):
    keliling = (2 * alas) + tinggi
    luas = 1/2 * alas * tinggi
    
    print('Keliling:', keliling,'\nLuas:', luas)

def persegi(sisi):
    keliling = sisi * 4
    luas = sisi * sisi
    
    print('Keliling:', keliling,'\nLuas:', luas)

x = input('Pilih bangun datar: \n 1. Persegi Panjang \n 2. Segitiga \n 3. Persegi \n input: ')
if x == '1':
    p = int(input('panjang: '))
    l = int(input('lebar: '))
    persegipanjang(p, l)
elif x == '2':
    a = int(input('alas: '))
    t = int(input('tinggi: '))
    segitiga(a, t)
elif x == '3':
    s = int(input('sisi: '))
    persegi(s)