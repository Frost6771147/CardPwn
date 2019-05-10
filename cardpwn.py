import os
import sys
import requests
import subprocess
from googlesearch import search


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m' # white

version = '1.3'

def banner():
	os.system('clear')
	banner = r'''
 _____               _______
/  __ \             | | ___ \
| /  \/ __ _ _ __ __| | |_/ /_      ___ __
| |    / _` | '__/ _` |  __/\ \ /\ / / '_ \
| \__/\ (_| | | | (_| | |    \ V  V /| | | |
 \____/\__,_|_|  \__,_\_|     \_/\_/ |_| |_|'''
	print(G + banner + W + '\n')
	print(G + '[>] ' + R + 'Created by : ' + W + 'Hacker Destination')
	print(G + '[>] ' + R + 'Version : ' + W + version)

def updater():
	print (G + '[+]' + R + ' Checking for updates...' + W + '\n')
	updated_version = requests.get('https://raw.githubusercontent.com/itsmehacker/cardpwn/master/version.txt', timeout = 5)
	updated_version = updated_version.text.split(' ')[1]
	updated_version = updated_version.strip()
	if updated_version != version:
		print (G + '[!]' + R + ' A New Version is Available : ' + W + updated_version)
		ans = input(G + '[!]' + R + ' Update ? [y/n] : ' + W)
		if ans == 'y':
			print ('\n' + G + '[+]' + R + ' Updating...' + '\n' + W)
			subprocess.check_output(['git', 'reset', '--hard', 'origin/master'])
			subprocess.check_output(['git', 'pull'])
			print (G + '[+]' + R + ' Script Updated...Please Execute Again...' + W)
			exit()
	else:
		print (G + '[+]' + R + ' Script is up-to-date...' + '\n' + W)

def cardpwn():
	urls = []
	qlist = []
	website = []
	paste_sites = ['cl1p.net', 'dpaste', 'dumpz.org', 'hastebin', 'ideone', 'pastebin', 'pw.fabian-fingerle.de','gist.github.com','https://www.heypasteit.com/','ivpaste.com','mysticpaste.com','paste.org.ru','paste2.org','sebsauvage.net/paste/','slexy.org','squadedit.com','wklej.se','textsnip.com']
	card = input(G + '[+] ' + R +'Enter Card No. -> ' + W)
	try:
		val = int(card)
		if len(str(val)) >= 12 and len(str(val)) <= 19:
			for site in paste_sites:
				query = '{} {}'.format(site, card)
				qlist.append(query)
			for entry in qlist:
				for url in search(entry, pause=2.0, stop=20, user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'):
					urls.append(url)

			print('\n' + G + '[>]' + R + ' Getting Dumps...' + W + '\n')
			for item in urls:
				for site in paste_sites:
					if '{}'.format(site) in item:
						print(G + '[+] ' + C + item + W)

		else:
			print('\n' + R + '[!] ' + G + 'Invaild Card Number' + W + '\n')
			return cardpwn()
			total = len(urls)
			if total == 0:
				print (R + '[-] No Open Leaks for this Card Number Found.' + W + '\n')
			else:
				print('\n' + G + '[+]' + R + ' Total Dumps Found : ' + W + str(total) + '\n')

	except ValueError:
		print('\n' + R + '[!] Invaild Card Number Entered...' + W + '\n')


def network():
	try:
		requests.get('https://github.com/', timeout = 5)
		print ('\n' + G + '[+]' + R + ' Checking Internet Connection...' + W, end = '')
		print (G + ' Working' + W + '\n')
	except requests.ConnectionError:
		print (R + '[!]' + R + ' You are Not Connected to the Internet...Quiting...' + W)
		sys.exit()

try:
	banner()
	network()
	updater()
	cardpwn()
except KeyboardInterrupt:
	print ('\n' + R + '[!]' + R + ' Keyboard Interrupt.' + W)
	exit()
