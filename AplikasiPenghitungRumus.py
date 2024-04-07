def hitung_luas_segitiga():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    print("Luas segitiga adalah:", luas)

def hitung_luas_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar
    print("Luas persegi panjang adalah:", luas)

def cek_ganjil_genap():
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(angka, "adalah angka genap")
    else:
        print(angka, "adalah angka ganjil")

while True:
    print("\nPilih menu:")
    print("1. Hitung luas segitiga")
    print("2. Hitung luas persegi panjang")
    print("3. Menentukan angka ganjil dan genap")
    print("4. Quit")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        hitung_luas_segitiga()
    elif pilihan == '2':
        hitung_luas_persegi_panjang()
    elif pilihan == '3':
        cek_ganjil_genap()
    elif pilihan == '4':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")