from colorama import init
from colorama import Fore
import mega_ddos
import colorama
colorama.init()

print(f"{Fore.MAGENTA} no skids allowed (; + """"

 ▄████▄   ▄▄▄       ██▓███  
▒██▀ ▀█  ▒████▄    ▓██░  ██▒
▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒
▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░
░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░
  ░  ▒     ▒   ▒▒ ░░▒ ░     
░          ░   ▒   ░░       
░ ░            ░  ░         
░                                             
    """)
print(f"{Fore.MAGENTA}1) ddos...")
print(f"{Fore.MAGENTA}2) rat...")
print(f"{Fore.MAGENTA}3) stats...")
print(f"{Fore.MAGENTA}+ enjoy (;")

choice = input(f"{Fore.RED} choose: ")
print(f"{Fore.RESET} nice choice!")

if choice == "1":
    mega_ddos.start()
    
