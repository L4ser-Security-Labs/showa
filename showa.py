#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "L4ser Secruity Labs"
__DATE__	= "15/06/2020"
__VERSION__	= "0.0.1"
__GITHUB__	= "https://github.com/L4ser-Security-Labs"

'''External Resource Monitor'''

"""
    Copyright (C) 2020 L4ser Security Labs
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

from sys import path, argv
import argparse
import colorama
from colorama import Fore, Style
import requests
import smtplib
path.append("src")
from decouple import config
SENDER = config('SENDER')
PASSWORD = config('PASSWORD')
smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login(SENDER, PASSWORD)



parser = argparse.ArgumentParser(description = "External Resource Monitor",\
				add_help = False)

parser.add_argument("-h", "--help", help = "Shows this message and exits",\
			action = "store_true")

parser.add_argument("-r", help = "Path to resources.showa file", 
                    type = str)

parser.add_argument("-e", help = "Email address to recieve notifications",
                    type = str)


args = parser.parse_args()

def validate_email(email):
    import re
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return True
    else:
        return False

def monitor_resources(showa_filepath):
    try:
        file = open(showa_filepath, 'r') 
        resources = file.readlines() 		
        count = 0 
        for resource in resources: 
            r = requests.get(resource.strip())
            if r.status_code != 200:
                SUBJECT = "SHOWA: Resource Unavailable"
                recipient = args.e
                text = """Resource {} is unavailable with a status of {}""".format(resource, r.status_code)
                message = "Subject: {}\n\n{}".format(SUBJECT, text)
                smtp_server.sendmail(SENDER, recipient, message)
        smtp_server.close()
    except Exception as error:
        SUBJECT = "Showa: Deployment Error"
        recipient = args.e
        text = "SHOWA ERROR: ", error
        message = "Subject: {}\n\n{}".format(SUBJECT, text)
        smtp_server.sendmail(SENDER, recipient, message)
        smtp_server.close()
        
    
if __name__ == "__main__":
	import banner
	
	if len(argv) <= 1:
		parser.print_help()
		exit()
	else:
		if args.help == True:
			parser.print_help()
			exit()
		else:
			if args.r == None:
				parser.print_help()
				print(Style.RESET_ALL)		
				print(Fore.RED + "\nShowa: Error: argument -r is required\n")
				print(Style.RESET_ALL)					
				exit()
			if args.e == None:	
				parser.print_help()
				print(Style.RESET_ALL)		
				print(Fore.RED + "\nShowa: Error: argument -e is required\n")
				print(Style.RESET_ALL)					
				exit()
			else:
				pass
	print("\n")
	print("*" * 75)
	
	if args.r[:15] != "resources.showa":
		print(Style.RESET_ALL)		
		print(Fore.RED + "\nShowa: Error: your file should be named resources.showa\n")
		print(Style.RESET_ALL)
		parser.print_help()
		exit()
	if args.e:
		if validate_email(args.e) == True:
			print(Style.RESET_ALL)		
			print(Fore.BLUE + "[+] Showa initialized...")
			print(Fore.BLUE + "[+] Check email for notifications")
			print(Style.RESET_ALL)				
			monitor_resources(args.r)
		elif validate_email(args.e) == False:
			print(Style.RESET_ALL)		
			print(Fore.RED + "\nInvalid Email address\n")
			print(Style.RESET_ALL)
		
