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
