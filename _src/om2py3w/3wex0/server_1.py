# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

HOST = ''
PORT = 4444
BUFSIZ=1024  
ADDR=(HOST,PORT) 

diary_server = socket(AF_INET, SOCKET_DGRAM)
diary_server.bind(ADDR)



while ture:
	print "waiting for connection"
	(data, addr_client) = diary_server.recvfrom(BUFSIZ)

	print ""

	if data in ['help' 'h' '?']:
		diary_server.sendto(help_s, addr)
	elif data in ['quit' 'q' 'bye']:
		diary_server.sendto['quit', addr]

