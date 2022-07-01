import sys
import socket
import threading
import datetime
from colorama import Fore

sys.path.insert(0, './easy-samp-query')
import query

# Socket server
class HidraCloner:
	def __init__(self, bind_address, bind_port, target_address, target_port):
		self.server = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

		self.bind_address = bind_address
		self.bind_port = bind_port
		self.target_address = target_address
		self.target_port = target_port

		self.query_info = query.send_query(target_address, target_port, 'i', 5)
		self.query_rules = query.send_query(target_address, target_port, 'r', 5)

	def listening(self):
		while(True):
			data = self.server.recvfrom(1024)
			address = data[1]
			opcode = chr(data[0][10])

			if opcode == 'p':
				self.server.sendto(data[0], address)

			elif opcode == 'i':
				self.server.sendto(data[0] + self.query_info, address)

			elif opcode == 'r':
				self.server.sendto(data[0] + self.query_rules, address)

			print(f'[{datetime.datetime.now()}]: QUERY: {Fore.RED}{opcode}{Fore.WHITE} by {address[0]}:{address[1]}')

	def refresh(self):
		self.query_info = query.send_query(self.target_address, self.target_port, 'i', 5)
		self.query_rules = query.send_query(self.target_address, self.target_port, 'r', 5)

	def start(self):
		self.server.bind((self.bind_address, self.bind_port))

		listen_thread = threading.Thread(target = self.listening)
		listen_thread.start()

		print(f"\n{Fore.GREEN}[+]{Fore.WHITE} Listening on {self.bind_address}:{self.bind_port}, cloning {self.target_address}:{self.target_port}")

	def stop(self):
		self.server.shutdown()


if __name__ == '__main__':
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
     
	server = HidraCloner('0.0.0.0', 7777, '51.254.21.27', 7777)
	server.start()