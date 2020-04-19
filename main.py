import os
import time
import socket
import threading
from colorama import init, Fore, Style

# Modules
import utils
import query
import config

# Socket server
class CloneQuery:
	def __init__(self, bind_address, bind_port, target_address, target_port):
		self.server = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

		self.bind_address = bind_address
		self.bind_port = bind_port
		self.target_address = target_address
		self.target_port = target_port

		self.query_info = query.SendQueryRequest(target_address, target_port, 'i')
		self.query_rules = query.SendQueryRequest(target_address, target_port, 'r')

	def listening(self):
		while(True):
			data = self.server.recvfrom(1024)
			address = data[1]
			opcode = utils.ReturnChar(data[0][10])

			if opcode == 'p':
				self.server.sendto(data[0], address)

			elif opcode == 'i':
				self.server.sendto(data[0] + self.query_info, address)

			elif opcode == 'r':
				self.server.sendto(data[0] + self.query_rules, address)

			utils.log_query(opcode, address)

	def refresh(self):
		self.query_info = query.SendQueryRequest(self.target_address, self.target_port, 'i')
		self.query_rules = query.SendQueryRequest(self.target_address, self.target_port, 'r')


	def start(self):
		self.server.bind((self.bind_address, self.bind_port))

		listen_thread = threading.Thread(target = self.listening)
		listen_thread.start()

		print(f"\n{Fore.GREEN}[+]{Fore.WHITE} Listening on {self.bind_address}:{self.bind_port}, cloning {self.target_address}:{self.target_port}")


	def stop(self):
		self.server.shutdown()


if __name__ == '__main__':
	utils.print_banner()

	server = CloneQuery(config.SERVER_IP, config.SERVER_PORT, config.CLONE_SERVER_IP, config.CLONE_SERVER_PORT)
	server.start()