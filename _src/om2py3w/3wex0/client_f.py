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


diary = open('diary.txt')
content = diary.read()
diary_client.sendto(content, ADDR)
diary.close()


# (recv, addr) = diary_client.recvfrom(BUFSIZ)

#print "recv %r, from %r " % (recv.decode('UTF-8'), addr)

diary_client.close()
