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

diary_server = socket(AF_INET, SOCK_DGRAM)
diary_server.bind(ADDR)


print "waiting for connection"
(data, addr_client) = diary_server.recvfrom(BUFSIZ)

content = data.decode('UTF-8')
print addr_client
# print " the address %r" % addr_client  转换不了
print data



	

