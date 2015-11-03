# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

def send_history():
    diary = open('diary.txt')
    content = diary.read()
    content = content.decode('UTF-8').encode('UTF-8')
    diary_server.sendto(byte(content), addr_client)
    diary.close()

def foo():
    HOST = ''
    PORT = 4444
    BUFSIZ=1024  
    ADDR=(HOST,PORT) 

    diary_server = socket(AF_INET, SOCK_DGRAM)
    diary_server.bind(ADDR)


    diary = open('diary.txt', 'a+', 0) #with statemanet / flush

    # while True:
    print "waiting for connection"
    (data, addr_client) = diary_server.recvfrom(BUFSIZ)

    content = data.decode('UTF-8')
    print "the text are:\n %s" % content
        '''print "conncetd from %r, message: %r" % (addr_client, content)
        diary.write(data)
        diary.write('\n')

        diary_server.sendto(data, addr_client) '''

        


if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()