#!/usr/bin/env python3
import sys
import socket
from datetime import datetime

def usage():
	print("[*] Usage:")
	print("bangrab [REMOTE HOST]")

def scan(ip):
	for port in range(1,10000):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			response = sock.connect_ex((ip, port))
			if response == 0:
				# Store first text sent by daemon in 1024 sized buffer, usually denoting the service being run on the port
				banner = sock.recv(1024).decode()
				print("[+] Port {} open: {}".format(port, banner))
			sock.close()
		except KeyboardInterrupt:
			print("[-] Exiting")
			sys.exit()
		except socket.gaierror:
			print("[-] Hostname could not be resolved. Exiting")
			sys.exit()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()
		sys.exit()
	host = sys.argv[1]
	ip = socket.gethostbyname(host)
	start = datetime.now()
	scan(ip)
	end = datetime.now()
	net = end - start
	print("[*] Scan completed in {}".format(net))