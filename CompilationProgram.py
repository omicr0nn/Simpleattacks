#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import py_compile
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

def derle_python_kodlari(dosya_listesi, cikti_dizini=None, optimize=False):
    derlenenler = []
    hatalar = []

    for dosya in dosya_listesi:
        try:
            if not dosya.endswith('.py'):
                raise ValueError(f"{dosya} dosyası geçerli bir Python dosyası değil!")

            if not os.path.exists(dosya):
                raise FileNotFoundError(f"{dosya} dosyası bulunamadı!")

            cikti_dosya = os.path.join(cikti_dizini, os.path.basename(dosya) + 'c') if cikti_dizini else dosya + 'c'
            py_compile.compile(dosya, cikti_dosya, optimize=optimize)

            derlenenler.append(cikti_dosya)
        except Exception as e:
            hatalar.append((dosya, str(e)))

    return derlenenler, hatalar

def raporlama(derlenenler, hatalar):
    print("\nDerlenen dosyalar:")
    for dosya in derlenenler:
        print(f"- {os.path.abspath(dosya)}")

    if hatalar:
        print("\nDerleme hataları:")
        for dosya, hata in hatalar:
            print(f"- {dosya}: {hata}")

def main():
    print("Derleme Programına Hoş Geldiniz.")
    dosya_listesi = []
    cikti_dizini = None

    while True:
        dosya = input("Derlemek istediğiniz Python dosyasının adını girin (Çıkmak için 'q' ya da 'exit' yazın): ")
        if dosya.lower() in ('q', 'exit'):
            break
        
        dosya_listesi.append(dosya)

    if dosya_listesi:
        cikti_dizin_sec = input("Derleme çıktı dosyalarını farklı bir dizine kaydetmek ister misiniz? (E/H): ").lower().startswith('e')
        if cikti_dizin_sec:
            cikti_dizini = input("Çıktı dosyalarını hangi dizine kaydetmek istersiniz? (Varsayılan olarak mevcut dizine kaydedilir, boş bırakın): ")

        optimize_sec = input("Derleme optimizasyonunu etkinleştirmek istiyor musunuz? (E/H): ").lower().startswith('e')
        
        derlenenler, hatalar = derle_python_kodlari(dosya_listesi, cikti_dizini, optimize=optimize_sec)
        raporlama(derlenenler, hatalar)
    else:
        print("Derlenecek dosya bulunamadı.")

if __name__ == "__main__":
    main()
