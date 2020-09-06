import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter
import colorama
from colorama import Fore, init
from datetime import date
os.system("title [STEAM] GiftCard Generator - Matty#8952")
os.system("cls")
cantidad = input(f"{Fore.CYAN}How many giftcards do you want to generate?: {Fore.RESET}")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
print(f"{Fore.RED}Generating...{Fore.RESET}")
time.sleep(1)

if (int(cantidad)<=int(count)):
	print("Invalid input, closing...")
	time.sleep(2)
	sys.exit()
	pass

while(int(count)<int(cantidad)):
    Generated = random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits).upper() for _ in range(5))+"-"+random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    f= open(current_path+"/"+str("GiftCards")+str("")+".txt","a")
    f.write(Generated+"\n")
    print(f"{Fore.GREEN}Generated code: {Fore.RESET}"+ Generated)
    count+=1

input(f"\n{Fore.GREEN}Codes Has been generated. Saved in (GiftCards.txt){Fore.RESET}{Fore.RED}\nEnter to exit.{Fore.RESET}")
