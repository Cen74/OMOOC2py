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

input_c = raw_input(' > ')
data = input_c.decode('UTF-8').encode('UTF-8')

diary_client.sendto(data, ADDR)
(recv, addr) = diary_client.recvfrom(BUFSIZ)

print "recv %r, from %r " % (recv.decode('UTF-8'), addr)

diary_client.close()
