import sys
import socket
from datetime import datetime

# Usage prompt
def usage():
	print("[*] Usage:")
	print("portscan [REMOTE HOST]")

def scan(ip):
	for port in range(1,10000):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# Connect to host on port, get error message if any
			response = sock.connect_ex((ip, port))
			# No error
			if response == 0:
				print("[+] Port {} open".format(port))
			# Close socket for this iteration
			sock.close()
		except KeyboardInterrupt:
			# User presses Ctrl+C
			print("[-] ^C exiting")
			sys.exit()
		except socket.gaierror:
			# Error: couldn't resolve hostname
			print("[-] Hostname could not be resolved. Exiting")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()
		sys.exit()
	host = sys.argv[1]
	ip = socket.gethostbyname(host)
	# Start scan
	start_time = datetime.now()
	scan(ip)
	# Scan ended
	end_time = datetime.now()
	time_taken = end_time - start_time
	print("[*] Scan completed in {}".format(time_taken))