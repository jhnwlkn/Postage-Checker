from Splash import SplashHias
import os, time
import uap


def login(username,password):
    sukses = False
    file = open("loginAkun.txt", "r")
    for i in file:
        a = i.split(",")
        if(a[0]==username and a[1]==password):
            sukses = True
            break
    file.close()
    if (sukses):
        SplashHias.splashLogin()
        print("-"*20)
        print("Login berhasil!!")
        print("-"*20)
        uap.main()
        
    else:
        print("-"*70)
        print("    Username/Password Salah !!!")
        print("-"*70)
        time.sleep(3)
        os.system('cls')
        awal()

def daftar(username,password):
    file = open("loginAkun.txt", "a")
    file.write("\n"+username+","+password)

def access(pilih):
    global username
    if pilih == 1 :
        os.system('cls')
        SplashHias.splashLogin()
        print("")
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        login(username,password)
    elif pilih == 2 :
        os.system('cls')
        SplashHias.splashBye()
        time.sleep(3)


def awal():
    os.system('cls')
    global pilih
    SplashHias.splashName()
    print("")
    print("-"*32)
    print("| SELAMAT DATANG DI MYONGKIRUY | ")
    print("| [1] LOGIN\t\t       | ")
    print("| [2] Exit\t\t       | ")
    print("-"*32)
    try :
        pilih = int(input("\nMasukkan Pilihan Anda : "))
        if pilih == 1 :
            access(1)
        else :
            access(2)
    except :
        os.system('cls')
        print("\nHarap Masukkan Pilihan (Angka).")
        time.sleep(3)
        awal()

awal()
# access(pilih)
# login("johnwilken", "2117051024")
