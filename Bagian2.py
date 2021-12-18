def persegipanjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar

    return keliling, luas

def segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi
    keliling = (2 * alas) + tinggi

    return keliling, luas

def persegi(sisi):
    luas = sisi * sisi
    keliling = sisi * 4

    return keliling, luas

x = input('Pilih bangun datar: ')
if x == 'persegipanjang':
    panjang = input('panjang: ')
    lebar = input('lebar: ')
    print(keliling, luas)
