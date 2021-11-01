#Program Kasir untuk Menghitung Jumlah Pesanan Pelanggan
def intro():
    print ("=======================================")
    print ("     Selamat Datang di Cafe ABC123     ")
    print ("=======================================")
    print ("Silahkan Pilih Menu")
intro ()

list_menu_makanan = ["Kentang Goreng", "Pisang Keju", "Roti Bakar", "Batagor", "Siomay"]
list_menu_minuman = ["Hazzelnut Chocolate", "Caramel Latte", "Air Mineral", "Cappucino", "Es Teh"]
list_harga_makanan = [20000, 15000, 15000, 20000, 15000]
list_harga_minuman = [10000, 15000, 5000, 15000, 8000]

def menu_makanan():
    print ("1. Kentang Goreng : Rp. 20.000")
    print ("2. Pisang Keju    : Rp. 15.000")
    print ("3. Roti Bakar     : Rp. 15.000")
    print ("4. Batagor        : Rp. 20.000")
    print ("5. Siomay         : Rp. 15.000")
    print ("=======================================")

def menu_minuman():
    print ("1. Hazzelnut Chocolate  : Rp. 10.000")
    print ("2. Caramel Latte        : Rp. 15.000")
    print ("3. Air Mineral          : Rp. 5.000")
    print ("4. Cappucino            : Rp. 15.000")
    print ("5. Es Teh               : Rp. 8.000")
    print ("=======================================")

def diskon_makan():
    if jumlah_pesan >= 2:
        hitung = harga * 5 / 100
        hitung_diskon = harga - hitung
    else:
        hitung_diskon = harga
    bayar = input("Pilih Metode Pembayaran [Tunai/E-Money] ? ")
    if bayar == "E-Money":
        print("Selamat Anda Mendapatkan Diskon sebesar 5 %")
        total = hitung_diskon * 5 / 100
        total_diskon = hitung_diskon - total
    elif bayar == "Tunai":
        print("Maaf Anda Belum Mendapatkan Diskon")
        total = hitung_diskon * 1
        total_diskon = total
    import datetime
    print ("=======================================")
    x = datetime.datetime.now()
    print(x)
    weekno = datetime.datetime.today().weekday()
    print(x.strftime("Hello %A"))
    if weekno < 5:
        print("This is Weekdays")
        print("Selamat Anda Mendapatkan Diskon Weekdays sebesar 10 %")
        akhir = total_diskon * 10 / 100
        total_akhir = total_diskon - akhir
    else: 
        print("This is Weekend")
        print("Selamat Anda Mendapatkan Diskon Weekends sebesar 5 %")
        akhir = total_diskon * 5 / 100
        total_akhir = total_diskon - akhir
    print ("=======================================")
    print ("             Cafe ABC123               ")
    print ("=======================================")
    print ("Menu                :",list_pesan)
    print ("Jumlah Pesanan      :",jumlah_pesan)
    print ("Harga               : Rp.",harga)
    print ("Diskon Pesanan      : Rp.",hitung_diskon)
    print ("=======================================")
    print ("Metode Pembayaran   :",bayar)
    print ("Diskon Pembayaran   : Rp.",total_diskon)
    print ("Diskon Harian       : Rp.",total_akhir)
    print ("Total yang Dibayar  : Rp.",total_akhir)

def diskon_minum():
    if jumlah_pesan >= 3:
        hitung = harga * 10 / 100
        hitung_diskon = harga - hitung
    else:
        hitung_diskon = harga
    bayar = input("Pilih Metode Pembayaran [Tunai/E-Money] ? ")
    if bayar == "E-Money":
        print("Selamat Anda Mendapatkan Diskon sebesar 5 %")
        total = hitung_diskon * 5 / 100
        total_diskon = hitung_diskon - total
    elif bayar == "Tunai":
        print("Maaf Anda Belum Mendapatkan Diskon")
        total = hitung_diskon * 1
        total_diskon = total
    import datetime
    print ("=======================================")
    x = datetime.datetime.now()
    print(x)
    weekno = datetime.datetime.today().weekday()
    print(x.strftime("Hello %A"))
    if weekno < 5:
        print("This is Weekdays")
        print("Selamat Anda Mendapatkan Diskon Weekdays sebesar 10 %")
        akhir = total_diskon * 10 / 100
        total_akhir = total_diskon - akhir
    else: 
        print("This is Weekend")
        print("Selamat Anda Mendapatkan Diskon Weekends sebesar 5 %")
        akhir = total_diskon * 5 / 100
        total_akhir = total_diskon - akhir
    print ("=======================================")
    print ("             Cafe ABC123               ")
    print ("=======================================")
    print ("Menu                :",list_pesan)
    print ("Jumlah Pesanan      :",jumlah_pesan)
    print ("Harga               : Rp.",harga)
    print ("Diskon Pesanan      : Rp.",hitung_diskon)
    print ("=======================================")
    print ("Metode Pembayaran   :",bayar)
    print ("Diskon Pembayaran   : Rp.",total_diskon)
    print ("Diskon Harian       : Rp.",total_akhir)
    print ("Total yang Dibayar  : Rp.",total_akhir)

jawab = "y"
while jawab == "y":
    print ("A. Menu Makanan")
    print ("B. Menu Minuman")
    pilihan = str(input("Masukkan Pilihan Menu [A/B] : "))
    print ("=======================================")
    if pilihan == "A":
        menu_makanan()
        pesan = int(input("Masukkan Pesanan Anda : "))
        jumlah_pesan = int(input("Masukkan Jumlah Pesanan : "))
        if pesan == 1:
            list_pesan = list_menu_makanan[0]
            harga = int(list_harga_makanan[0] * jumlah_pesan)
        elif pesan == 2:
            list_pesan = list_menu_makanan[1]
            harga = int(list_harga_makanan[1] * jumlah_pesan)
        elif pesan == 3:
            list_pesan = list_menu_makanan[2]
            harga = int(list_harga_makanan[2] * jumlah_pesan)
        elif pesan == 4:
            list_pesan = list_menu_makanan[3]
            harga = int(list_harga_makanan[3] * jumlah_pesan)
        elif pesan == 5:
            list_pesan = list_menu_makanan[4]
            harga = int(list_harga_makanan[4] * jumlah_pesan)
        print("Pesanan Anda adalah",list_pesan, "sebanyak",jumlah_pesan, "porsi")
        if jumlah_pesan >= 2:
            print("Selamat Anda Mendapatkan Diskon sebesar 5 %")
            print ("=======================================")
            diskon_makan()
        else:
            print("Maaf Anda Belum Mendapatkan Diskon")
            print ("=======================================")
            diskon_makan()
    elif pilihan == "B":
        menu_minuman()
        pesan = int(input("Masukkan Pesanan Anda : "))
        jumlah_pesan = int(input("Masukkan Jumlah Pesanan : "))
        if pesan == 1:
            list_pesan = list_menu_minuman[0]
            harga = int(list_harga_minuman[0] * jumlah_pesan)
        elif pesan == 2:
            list_pesan = list_menu_minuman[1]
            harga = int(list_harga_minuman[1] * jumlah_pesan)
        elif pesan == 3:
            list_pesan = list_menu_minuman[2]
            harga = int(list_harga_minuman[2] * jumlah_pesan)
        elif pesan == 4:
            list_pesan = list_menu_minuman[3]
            harga = int(list_harga_minuman[3] * jumlah_pesan)
        elif pesan == 5:
            list_pesan = list_menu_minuman[4]
            harga = int(list_harga_minuman[4] * jumlah_pesan)
        print("Pesanan Anda adalah",list_pesan, "sebanyak",jumlah_pesan, "gelas")
        if jumlah_pesan >= 3:
            print("Selamat Anda Mendapatkan Diskon sebesar 10 %")
            print ("=======================================")
            diskon_minum()
        else:
            print("Maaf Anda Belum Mendapatkan Diskon")
            print ("=======================================")
            diskon_minum()
    jawab = input("Apakah Anda Ingin Memesan Kembali [y/t] ? ")