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
os.system("clear");
print("Loading.");
time.sleep(2);
os.system("clear");
print("Loading..");
time.sleep(2);
os.system("clear");
print("Loading...");
time.sleep(2);
print("Loading..");
os.system("clear");
time.sleep(2);
os.system("clear");
print(Fore.RED + text);
print("\n\n\n");
print(Fore.RED+"[1]"+Fore.WHITE+" Phone Search");
print(Fore.RED+"[2]"+Fore.WHITE+" IP Search");
print(Fore.RED+"[3]"+Fore.WHITE+" Exit");
user_input = input("Введите Число : ");
if "1" in user_input.lower():
 os.system("clear");
 print(Fore.RED + text);
 print(Fore.GREEN+" Вы выбрали Поиск По номеру !");
 phone_num = input(Fore.YELLOW + "  Введите Номер +7 : ");
 if phone_num.lower():
  print(Fore.RED+"Вы выбрали номер : +7"+phone_num);
  print(Fore.GREEN+"ФИО :");
  print(Fore.GREEN+"Номер : +7"+phone_num);
  
if "2" in user_input.lower():
  print(Fore.RED +"Вы выбрали поиск По ИП");

if "3" in user_input.lower():
  print(Fore.RED +"Вы Вышли Из Системы!");
  os.system("exit");

