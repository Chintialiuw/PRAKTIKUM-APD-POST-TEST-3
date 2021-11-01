#Program Log In Sederhana
list_isi = ["Bambang Susanto", "akuinisiapa123"]

def intro():
    print ("=======================================")
    print ("    Selamat Datang di telurbadak.id    ")
    print ("=======================================")
intro()

def penentu():
    for x in range(3):
        print ("=======================================")
        nama_pengguna = input("Username            : ")
        kata_kunci = input("Password            : ")
        if nama_pengguna == list_isi[0] and kata_kunci == list_isi[1]:
            print ("----------------Loading----------------")
            print ("Log In Sukses... Selamat Datang",list_isi[0])
            print ("=======================================")
            exit()
        elif nama_pengguna != list_isi[0] or kata_kunci == list_isi[1]:
            print ("----------------Loading----------------")
            print("Maaf Username yang Anda Masukkan Tidak Terdaftar")
            print ("=======================================")
        elif nama_pengguna == list_isi[0] or kata_kunci != list_isi[1]:
            print ("----------------Loading----------------")
            print("Maaf Password yang Anda Masukkan Salah")
            print("=======================================")
    print("Maaf Anda Gagal Log In")
    print ("=======================================")
    exit()

def akun():
    akun = input("Sudah Mempunyai Akun [y/t] ? ")
    print ("=======================================")
    if akun == "y":
        print ("------------Silahkan Log in------------")
        penentu()
    elif akun == "t":
        print ("Silahkan Membuat Akun terlebih dahulu")
akun()

def akun_baru():
    nama_id = input("Username            : ")
    kata_sandi0 = input("Password            : ")
    kata_sandi1 = input("Konfirmasi Password : ")
    print ("=======================================")
    yakin = input("Apakah sudah yakin [y/t] ? ")
    print ("=======================================")
    if yakin == "y":
        print ("----------------Loading----------------")
        if kata_sandi0 == kata_sandi1:
            print("Selamat",nama_id, ", Akun Anda Berhasil Tersimpan")
            print ("=======================================")
            print("------------Silahkan Log in------------")
            list_isi[0] = nama_id
            list_isi[1] = kata_sandi0
            penentu()

        elif kata_sandi0 != kata_sandi1:
            print("Password yang Anda Masukkan Tidak Sesuai")
            print ("=======================================")
            ulang = str(input("Ingin Mengulang Kembali [y/t] ? "))
            if ulang == "y":
                akun_baru()
                exit()
            elif ulang == "t":
                exit()
    elif yakin == "t":
        print ("=======================================")
        print("Isikan Kembali Data secara Benar!")
        akun_baru()
        exit()
akun_baru()