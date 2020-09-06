#This is a simple STEAM GiftCard generator Made by me :D
#Im new in coding, if u want to help me: Matty#8952 (my discord)
#Coded in 5/7/2020
#Github: /MattyTM
#Twitch: /matiduszkin
#Feel free to use.
#if u repost pls give credits :D
import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter
import colorama
from colorama import Fore, init
from datetime import date

os.system("title [STEAM] GiftCard Generator - Matty#8952") #Title of the app
os.system("cls")
cantidad = input(f"{Fore.CYAN}How many giftcards do you want to generate?: {Fore.RESET}") #The amount of codes
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
print(f"{Fore.RED}Generating...{Fore.RESET}") #a generating msg
time.sleep(1)

if (int(cantidad)<=int(count)):
	print("Invalid input, closing...") #If Input is < or = to 0 Print invalid and close (2sec delay)
	time.sleep(2)
	sys.exit()
	pass

while(int(count)<int(cantidad)):
    Generated = random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits).upper() for _ in range(4))+"-"+random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    f= open(current_path+"/"+str("GiftCards")+str("")+".txt","a") #This generate codes
    f.write(Generated+"\n")
    print(f"{Fore.GREEN}Generated code: {Fore.RESET}"+ Generated) #Prints the generated code in the screen
    count+=1

input(f"\n{Fore.GREEN}Codes Has been generated. Saved in (GiftCards.txt){Fore.RESET}{Fore.RED}\nEnter to exit.{Fore.RESET}")
#A custom final msg !