#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Wordlist Olustur")
print("""
Wordlist Oluşturma Programına Hoş Geldiniz.
""")

minimumkarakter = input("Minimum Karakter Sayısını Girin: ")
maksimumkarakter = input("Maksimum Karakter Sayısını Girin: ")
karakter = input("İstediğiniz Karakterleri Girin: ")
kayityeri = input("Kaydedilecek Yeri Girin: ")

os.system("crunch " + minimumkarakter + " " + maksimumkarakter + " " + karakter + " -o " + kayityeri)

print("İşlem Başarıyla Tamamlandı.")
