#!/usr/bin/env bash

echo "Output to /tmp/recon.txt"

echo "New intranet scan" | tee >> /tmp/recon.txt

for ip0 in $(seq 0 255)
do
	for ip1 in $(seq 0 255)
	do
		for ip2 in $(seq 0 255)
		do
			for ip3 in $(seq 0 255)
			do
				ip="$ip0.$ip1.$ip2.$ip3"
				ping -c 1 $ip -W 3 > /dev/null
				if [ $? = 0 ]
				then
					echo "$ip was up" | tee >> /tmp/recon.txt
					echo "Port scanning host $ip" | tee >> recon.txt
					./portscan.py $ip
					echo "Banner scanning host $ip" | tee >> recon.txt
					./bangrab.py $ip
				fi
			done
		done
	done
done