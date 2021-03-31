#!/usr/bin/python3
import requests
import sys
from colorama import Fore, Style

def red(text):
	red_text = Fore.RED + text + Style.RESET_ALL
	return red_text

def green(text):
	green_text = Fore.GREEN + text + Style.RESET_ALL
	return green_text

def cyan(text):
	cyan_text = Fore.CYAN + text + Style.RESET_ALL
	return cyan_text

def ipInfo(ip_list):
	for i,ip in enumerate(ip_list):
		r = requests.get('https://ipinfo.io/'+ip)
		data = r.json()
		if i > 0:
			print()
		if 'error' in data:
			print(red(data['error']['message']))
		if 'bogon' in data:
			print(red(ip + ' is a private IP address'))
		else:
			print(green('IP:'),data['ip'])
			#print(green('Hostname:'),data['hostname'])
			print(green('City:'),data['city'])
			print(green('Region:'),data['region'])
			print(green('Country:'),data['country'])
			print(green('Location:'),data['loc'])
			print(green('Google maps URL:'),cyan('https://google.com/maps/@'+data['loc']+',12z'))
			print(green('Org:'),data['org'])
			print(green('Postal code:'),data['postal'])
			print(green('Timezone:'),data['timezone'])

if len(sys.argv) > 1:
	ip_list = sys.argv[1:]
else:
	ip_list = ['']

ipInfo(ip_list)
