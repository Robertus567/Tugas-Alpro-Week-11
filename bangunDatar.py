def cari_panjang_persegi_panjang(luas=0, keliling=0, lebar=0):
    if luas != 0 and lebar != 0:
        return luas / lebar
    elif keliling != 0 and lebar != 0:
        return (keliling / 2) - lebar
    else:
        return "Data tidak cukup untuk menghitung panjang."
        
#cari lebar persegi panjang

def cari_lebar_persegi_panjang(panjang=0, luas=0, keliling=0):
    if luas != 0 and panjang != 0:
        return luas / panjang
    elif keliling != 0:
        return (keliling / 2) - panjang
    else:
        return "Data tidak cukup untuk menghitung lebar."



def cari_sisi_persegi(luas=0, keliling=0):
    if keliling != 0:
        return keliling / 4
    elif luas != 0:
        return luas ** 0.5  
    else:
        return "Data tidak cukup untuk menghitung sisi persegi."



def cari_radius_lingkaran(luas=0, keliling=0):
    if luas != 0:
        return (luas / 3.14) ** 0.5  
    elif keliling != 0:
        return keliling / (2 * 3.14)
    else:
        return "Data tidak cukup untuk menghitung radius lingkaran."


print("Pilih jenis perhitungan:")
print("1. Panjang Persegi Panjang")
print("2. Lebar Persegi Panjang")
print("3. Sisi Persegi")
print("4. Radius Lingkaran")

pilihan = int(input("Masukkan pilihan (1/2/3/4): "))

if pilihan == 1:
 
    luas = float(input("Masukkan luas (atau 0 jika tidak diketahui): "))
    lebar = float(input("Masukkan lebar (atau 0 jika tidak diketahui): "))
    keliling = float(input("Masukkan keliling (atau 0 jika tidak diketahui): "))
    hasil = cari_panjang_persegi_panjang(luas, keliling, lebar)
    print("Panjang Persegi Panjang:", hasil)

elif pilihan == 2:
 
    panjang = float(input("Masukkan panjang (atau 0 jika tidak diketahui): "))
    luas = float(input("Masukkan luas (atau 0 jika tidak diketahui): "))
    keliling = float(input("Masukkan keliling (atau 0 jika tidak diketahui): "))
    hasil = cari_lebar_persegi_panjang(panjang, luas, keliling)
    print("Lebar Persegi Panjang:", hasil)

elif pilihan == 3:
  
    luas = float(input("Masukkan luas (atau 0 jika tidak diketahui): "))
    keliling = float(input("Masukkan keliling (atau 0 jika tidak diketahui): "))
    hasil = cari_sisi_persegi(luas, keliling)
    print("Sisi Persegi:", hasil)

elif pilihan == 4:

    luas = float(input("Masukkan luas (atau 0 jika tidak diketahui): "))
    keliling = float(input("Masukkan keliling (atau 0 jika tidak diketahui): "))
    hasil = cari_radius_lingkaran(luas, keliling)
    print("Radius Lingkaran:", hasil)

else:
    print("Pilihan tidak valid.")
