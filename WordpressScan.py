#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from os import system

system("cls||clear")
def rainbow_text(text, delay=0.1):
    colors = [
    "\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m", "\033[37m",
    ]

    for i in range(len(text)):
        char = text[i]
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write("\033[0m")
    sys.stdout.write("\n")

def main():
    rainbow_text("Coding by omicr0n")
    sys.stdout.write("\033[37m")
    sys.stdout.write("Coding by Omicron\n")
	
if __name__ == "__main__":
    rainbow_text("Coding by omicr0n")

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS TARAMA")
print("""
Wordpress Tarama Programına Hoş Geldiniz. 

1) Hızlı Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Yönetici Kullanıcı Adı Tarama
""")

islemno = input("İşlem Numarasını Girin: ")

if(islemno=="1"):
	site = input("Site Adresi Girin: ")
	os.system("wpscan --url " + site)

elif(islemno == "2"):
	site = input("Site Adresi Girin: ")
	os.system("wpscan --url " + site + " --enumerate p")

elif(islemno == "3"):
	site = input("Site Adresi Girin: ")
	os.system("wpscan --url " + site + " --enumerate t")

elif(islemno == "4"):
	site = input("Site Adresi Girin: ")
	os.system("wpscan --url " + site + " --enumerate u")

else:
	print("Hatalı Seçim Yaptınız. Program Kapatılıyor.")
