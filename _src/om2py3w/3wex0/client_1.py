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

data = raw_input(' > ')

diary_client.sendto(data, ADDR)
(recv, addr) = diary_client.recvfrom(BUFSIZ)

print "recvfrom %s: %s " (addr, recv)

diary_client.close()
