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
os.system("figlet Kaba Kuvvet")
print("""
Kaba Kuvvet  Programına Hoş Geldiniz. 

1) FTP
2) SSH
3) Telnet
4) HTTP
5) SMB
6) RDP
7) VNC
8) SIP
9) Redis
10) PostgreSQL
11)MySQL
""")

islemno = input("İşlem No Girin: ")
hedefip = input("Hedef İp Girin: ")
kullaniciadi = input("Kullanıcı Adı Dosya Yolu: ")
sifre = input("Sifrelerin Bulunduğu Dosya Yolu: ")

if(islemno == "1"):
	os.system("ncrack -p 21 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

if(islemno == "2"):
	os.system("ncrack -p 22 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
