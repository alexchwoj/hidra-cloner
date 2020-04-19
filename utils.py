import os
import datetime
import platform
from colorama import init, Fore, Style

ip_list = []

# Banner & logging
def log_query(opcode, address):
	if not address[0] in ip_list:
		ip_list.append(address[0])
		log = open('ip_log.txt', 'a')
		log.write(f'{address[0]}\n')
		log.close()

	print(f'[{datetime.datetime.now()}]: QUERY: {Fore.RED}{opcode}{Fore.WHITE} by {address[0]}:{address[1]}')


def print_banner():
	if platform.system() == 'Windows':
		os.system('cls')
		init(convert = True)

	elif platform.system() == 'Linux':
		os.system('clear')

	print(f'''{Fore.CYAN}                          
 @@@  @@@  @@@  @@@@@@@   @@@@@@@    @@@@@@   
 @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
 @@!  @@@  @@!  @@!  @@@  @@!  @@@  @@!  @@@  
 !@!  @!@  !@!  !@!  @!@  !@!  @!@  !@!  @!@  
 @!@!@!@!  !!@  @!@  !@!  @!@!!@!   @!@!@!@!  
 !!!@!!!!  !!!  !@!  !!!  !!@!@!    !!!@!!!!  
 !!:  !!!  !!:  !!:  !!!  !!: :!!   !!:  !!!  
 :!:  !:!  :!:  :!:  !:!  :!:  !:!  :!:  !:!  
 ::   :::   ::   :::: ::  ::   :::  ::   :::  
  :   : :  :    :: :  :    :   : :   :   : :''' + Fore.WHITE)

# Query opcodes byte
def ReturnChar(dec):
	if dec == 105:
		return 'i'

	elif dec == 114:
		return 'r'

	elif dec == 99:
		return 'c'

	elif dec == 100:
		return 'd'

	elif dec == 120:
		return 'x'

	elif dec == 112:
		return 'p'