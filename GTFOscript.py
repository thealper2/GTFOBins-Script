import requests
import argparse
import colorama
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup

colorama.init(autoreset=True)

def banner():
	print("  ____ _____ _____ ____")                  
	print(" / ___|_   _|  ___/ ___|  ___ __ _ _ __ ") 
	print("| |  _  | | | |_  \\___ \\ / __/ _` | '_ \\ ")
	print("| |_| | | | |  _|  ___) | (_| (_| | | | |")
	print(" \\____| |_| |_|   |____/ \\___\\__,_|_| |_|\n")

def scan_binary(binary_):
	func = []
	code = []
	p_code = []

	bin_ = binary_
	url = requests.get(f"https://gtfobins.github.io/gtfobins/{bin_}")
	soup = BeautifulSoup(url.content, 'html.parser')
	
	for element in soup.find_all('h2'):
		func.append(element.text)
	print(f"{Style.BRIGHT}[!] {Back.RED}Function List")
	for element in range(len(func)):
		print(f"{Fore.RED}[*] {Fore.WHITE}{Style.BRIGHT}{func[element]}")
	print()

	for element in soup.select('.language-plaintext'):
		p_code.append(element.text)

	for element in soup.find_all('code'):
		if element.text not in p_code:
			code.append(element.text)

	for element in range(len(code)):
		print(f"{Style.BRIGHT}* {Back.RED}[{func[element].upper()}]")
		print()
		print(code[element])
		print(f'{Style.BRIGHT}----------------------------------------------')

def scan_function(binary_, function_):
	func = []
	code = []
	p_code = []

	bin_ = binary_
	url = requests.get(f"https://gtfobins.github.io/gtfobins/{bin_}")
	soup = BeautifulSoup(url.content, 'html.parser')
	
	for element in soup.find_all('h2'):
		func.append(element.text)
	print(f"{Style.BRIGHT}[!] {Back.RED}Function List")
	for element in range(len(func)):
		print(f"{Fore.RED}[*] {Fore.WHITE}{Style.BRIGHT}{func[element]}")
	print()

	for element in soup.select('.language-plaintext'):
		p_code.append(element.text)

	for element in soup.find_all('code'):
		if element.text not in p_code:
			code.append(element.text)

	for element in range(len(func)):
		if func[element] == function_:
			print(f"{Style.BRIGHT}* {Back.RED}[{func[element].upper()}]")
			print()
			print(code[element])
			print(f'{Style.BRIGHT}----------------------------------------------')

def scan():
	url = requests.get(f"https://gtfobins.github.io/")
	soup = BeautifulSoup(url.content, 'html.parser')
	binaries = soup.find_all(class_="bin-name")
	print(f"{Back.RED}{Style.BRIGHT}Binaries in GTFObins")
	for i in binaries:
		print(f"{Fore.RED}[-] {Fore.WHITE}{Style.BRIGHT}" + i.text)

	print("----------------------")
	binary_ = input(f"{Fore.RED}[!] {Fore.GREEN}BINARY> ")

	func = []
	code = []
	p_code = []

	url = requests.get(f"https://gtfobins.github.io/gtfobins/{binary_}")
	soup = BeautifulSoup(url.content, 'html.parser')

	for element in soup.find_all('h2'):
		func.append(element.text)
	print(f"{Style.BRIGHT}[!] {Back.RED}Function List")
	for element in range(len(func)):
		print(f"{Fore.RED}[*] {Fore.WHITE}{Style.BRIGHT}{func[element]}")
	print()

	for element in soup.select('.language-plaintext'):
		p_code.append(element.text)

	for element in soup.find_all('code'):
		if element.text not in p_code:
			code.append(element.text)

	for element in range(len(code)):
		print(f"{Style.BRIGHT}* {Back.RED}[{func[element].upper()}]")
		print()
		print(code[element])
		print(f'{Style.BRIGHT}----------------------------------------------')


argument_parser = argparse.ArgumentParser(description="GTFOBINS binary scan.")
argument_parser.add_argument('-b', '--binary', required=False, help='Binary name')
argument_parser.add_argument('-f', '--function', required=False, help='Function name')
arguments = argument_parser.parse_args()

if arguments.binary and not arguments.function:
	banner()
	scan_binary(arguments.binary)
elif arguments.binary and arguments.function:
	banner()
	scan_function(arguments.binary, arguments.function)
else:
	banner()
	scan()