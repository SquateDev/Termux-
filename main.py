import time 
import os
from colorama import Fore, Style
import subprocess 

text = """██████╗░███████╗░█████╗░███╗░░██╗░█████╗░███╗░░██╗
██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗████╗░██║
██║░░██║█████╗░░███████║██╔██╗██║██║░░██║██╔██╗██║
██║░░██║██╔══╝░░██╔══██║██║╚████║██║░░██║██║╚████║
██████╔╝███████╗██║░░██║██║░╚███║╚█████╔╝██║░╚███║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝"""
time.sleep(1);
print("Loading... |");
time.sleep(2);
print("Loading... /");
time.sleep(2);
os.system("clear");
print(Fore.RED + text);
print("\n\n\n");
print(Fore.RED+"[ 1 ]"+Fore.WHITE+" Phone Searc");
print(Fore.RED+"[ 2 ]"+Fore.WHITE+" IP Searc");
user_input = input("Введите Число : ");
if "1" in user_input.lower():
 os.system("clear");
 print(Fore.RED + text);
 print(Fore.RED+"Вы выбрали Поиск По номеру !");
 phone_num = input(Fore.RED + "Введите Номер +7 : ");
if "2" in user_input.lower():
  print(Fore.RED +"Вы выбрали поиск По ИП");


