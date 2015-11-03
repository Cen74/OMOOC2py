# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

HOST = 'localhost'  
PORT = 4444  
BUFSIZ = 1024  
ADDR = (HOST,PORT)  
  
diary_client = socket(AF_INET,SOCK_DGRAM) 


while True:
	input_c = raw_input(' > ')

	if input_c == 'help' or input_c == 'h' or input_c == '?':
		print """press \'q\' or \'quit\' \'bye\' for help
 
press  \'h\' or \'help\' or \'bye\' to exit"""
	elif input_c == 'bye' or input_c == 'q' or input_c == 'quit':
		print "bye"
		break
	else:
		data = input_c.decode('UTF-8').encode('UTF-8')

		diary_client.sendto(data, ADDR)
		(recv, addr) = diary_client.recvfrom(BUFSIZ)

		print "recv %r, from %r " % (recv.decode('UTF-8'), addr)

diary_client.close()
