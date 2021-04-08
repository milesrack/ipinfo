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
		r = requests.get('http://ip-api.com/json/'+ip)
		data = r.json()
		if i > 0:
			print()
		if 'fail' in data:
			print(red('Invalid IP address'))
		if 'private range' in data:
			print(red(ip + ' is a private IP address'))
		else:
			print(green('IP:'),data['query'])
			print(green('City:'),data['city'])
			print(green('Country:'),data['country'])
			print(green('Latitude:'),str(data['lat']))
			print(green('Longitude'),str(data['lon']))
			print(green('Google maps URL:'),cyan('https://google.com/maps/@'+str(data['lat'])+','+str(data['lon'])+',12z'))
			print(green('ISP:'),data['isp'])

if len(sys.argv) > 1:
	ip_list = sys.argv[1:]
else:
	ip_list = ['']

ipInfo(ip_list)
