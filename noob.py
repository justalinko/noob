#!/usr/bin/python

import os
import sys
import warna
biru=warna.color.BLUE
merah=warna.color.RED
kuning=warna.color.YELLOW
hijau=warna.color.GREEN
cian=warna.color.CYAN
encol=warna.color.ENDC
ungu=warna.color.PURPLE
bgputih=warna.color.backWhite
ul=warna.color.UNDERL
bold=warna.color.BOLD
print'''
        '''+merah+'''#############################################
        #############################################
        #                                          ####
        #            ###             ###           ####
        #   #    #  #   #           #   #  #####    #
        #   ##   # #     #         #     # #    #   #
        #   # #  # #  () #         #  () # #####    #'''+kuning+'''
        #   #  # # #     #         #     # #    #   #
        #   #   ##  #   #           #   #  #    #   #
        #   #    #   ###             ###   #####    #
        #                 #######                   #'''+hijau+'''
        #                 []   []                   #
        #                                           #
        #                                           #'''+cian+'''
##############################################################
# version :|       c0ded by : alinko-kun        | c0dename : #
#   v1.0   |       copyright (c) 2016           |  H3lp3rz   #
##############################################################
'''+encol
print(merah+"1  > Update")
print(kuning+"2  > Upgrade")
print(hijau+"3  > Install aplikasi")
print(cian+"4  > Ganti repository")
print(encol+"5  > Perbaiki error saat install")
print(ungu+"6  > Uninstall aplikasi")
print(ungu+"7  > Hapus aplikasi yang gagal install")
print(encol+"8  > Auto tambah repository ")
print(cian+"9  > Auto mempercantik terminal")
print(hijau+"10 > OS info")
print(kuning+"00 > Bantuan")
print(merah+"99 > Keluar")
def AutoGantiRepo(link,cuk,cik,cok):
    os.system("wget "+link+" -x")
    os.system("mv "+cuk+" /etc/apt/sources.list")
    os.system("rmdir "+cik)
    os.system("rmdir "+cok)
def AutoTerminalCantik():
    os.system("wget http://alinkoproject.com/n00b/figlet.txt")
    os.system("mv figlet.txt ../.bashrc")
def maindek():
        try:
                dek=kuning+"root"+merah+"@n00bz:~#"+hijau
                pil=raw_input(dek)
                if pil=="1":
                        os.system("apt-get update")
                        maindek()
                elif pil=="2":
                        os.system('apt-get upgrade')
                        maindek()
                elif pil=="3":
                        a=raw_input(cian+"root@"+biru+"n00bz:/aplikasi #"+merah)
                        if a:
                                os.system("apt-get install "+a)
                                maindek()
                        else:
                                print(kuning+"[!] Error :!"+encol)
                                maindek()
                elif pil=="4":
                       y=raw_input(biru+ul+"apakah anda yakin? (y/n)"+encol)
                       if y=="Y" or y=="y":
                                os.system("pico /etc/apt/sources.list")
                                maindek()
                       else:
                                print(merah+"[!] Anda kurang yakin.."+encol)
                                maindek()
                elif pil=="5":
                        yn=raw_input(biru+ul+"apakah anda yakin? (y/n)"+encol)
                        if yn=="Y" or yn=="y":
                                os.system("apt-get -f install")
                                maindek()
                        else:
                                print(encol+"[!]"+merah+"anda kurang yakin.."+encol)
                                maindek()
                elif pil=="6":
                        app=raw_input(cian+"root@"+biru+"n00bz:/aplikasi #"+merah)
                        if app:
                                os.system("apt-get remove "+app)
                                maindek()
                        else:
                                print(encol+"[!]"+merah+"anda kurang yakin.."+encol)
                                maindek()
                elif pil=="7":
                        apx=raw_input(biru+ul+"apakah anda yakin? (y/n)"+encol)
                        if apx=="y" or apx=="Y":
                                os.system("apt-get autoremove")
                                maindek()
                        else:
                                print(encol+"[!]"+merah+"anda kurang yakin.."+encol)
                                maindek()
                elif pil=="8":
                        print(bgputih+"REPOSITORY YANG TERSDIA"+encol)
                        print(biru+"1  > Kali Linux"+encol)
                        print(kuning+"2  > Ubuntu"+encol)
                        print(merah+"3  > Debian"+encol)
                        print(hijau+"5  > Linux Mint"+encol)
                        repo=raw_input(cian+"root@"+biru+"n00bz:/repository #"+encol)
                        if repo=="1":
                                AutoGantiRepo('http://alinkoproject.com/n00b/kali.txt','alinkoproject.com/n00b/kali.txt','alinkoproject.com/n00b','alinkoproject.com')
                                print(merah+bold+ul+"[!] BERHASIL "+encol)
                                maindek()
                        elif repo=="2":
                                AutoGantiRepo('http://alinkoproject.com/n00b/ubuntu.txt','alinkoproject.com/n00b/ubuntu.txt','alinkoproject.com/n00b','alinkoproject.com')
                                print(merah+bold+ul+"[!] BERHASIL "+encol)
                                maindek()
                        elif repo=="3":
                                AutoGantiRepo('http://alinkoproject.com/n00b/debian.txt','alinkoproject.com/n00b/debian.txt','alinkoproject.com/n00b','alinkoproject.com')
                                print(merah+bold+ul+"[!] BERHASIL "+encol)
                                maindek()
                        elif repo=="4":
                                print(merah+bold+ul+"[!] REPOSITORY BELUM TERDEDIA.. "+encol)
                                print(kuning+"kontak : alinkokomansuby@gmail.com"+encol)
                                maindek()
                        else:
                                print(kuning+"pilihan anda tidak tersedia !"+encol)
                                maindek()
                elif pil=="9":
                        AutoTerminalCantik()
                        print(merah+bold+ul+"[!] BERHASIL "+encol)
                        maindek()
                elif pil=="99":
                        os.system("exit")
                elif pil=="00":
                        x=os.system('cat baca-aku-mas.txt')
                        if x==True:
                                os.system('cat baca-aku-mas.txt')
                        else:
                                print '''
                                Menggunakan : ./noob.py
                                            : python noob.py
                                            '''
                        maindek()
                elif pil=="10":
                     t=raw_input(biru+ul+"untuk melakukan hal ini,PC anda harus sudahh terinstall \"screenfetch\", \n apakah sudah terinstall? (y/n)"+encol)
                     if t=="n" or t=="N":
                         os.system("apt-get install screenfetch")
                         maindek()
                     else:
                        os.system("screenfetch")
                        maindek()
                        
        except(KeyboardInterrupt):
                print(kuning+"\n[!]"+hijau+" Memberhentikan program... ")
                print(hijau+"\n[+]"+kuning+"Terimakasih telah menggunakan! \n Ttd : alinko")
        else: 
                print(kuning+bold+ul+"[!] Tidak ada pilihan semacam ini =>"+pil+encol)
                print(merah+bold+"[!] Perintah salah.."+encol)
                maindek()
                
maindek()
