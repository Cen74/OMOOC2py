# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 



def foo():

	HOST = 'localhost'  
	PORT = 4444  
	BUFSIZ = 1024  
	ADDR = (HOST,PORT)  
  
	diary_client = socket(AF_INET,SOCK_DGRAM) 

	diary_client.sendto('-login', ADDR)
	(login_message, addr) = diary_client.recvfrom(BUFSIZ)
	print "Log in on server %s %s" % addr 
	print login_message

	while True:
		input_c = raw_input(' > ')

		if input_c in ['q', 'quit', 'bye']:
			print "bye"
			break
		elif input_c == 'syn':
			diary_client.sendto('syn', ADDR)
			history = diary_client.recv(BUFSIZ)
			print history
		elif input_c in ['help', 'h', '?']:
			print """
			  press \'q\' or \'quit\' \'bye\' for help
 
			  press  \'h\' or \'help\' or \'bye\' to exit

			  press syn to return history"""
		else:
			data = input_c
			diary_client.sendto(input_c, ADDR)
		
	diary_client.close()

if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()


'''
Traceback (most recent call last):
  File ".\client_3.py", line 51, in <module>
    foo()
  File ".\client_3.py", line 40, in foo
    diary_client.sendto(data, ADDR)
  File "D:\Python27\lib\socket.py", line 174, in _dummy
    raise error(EBADF, 'Bad file descriptor')
socket.error: [Errno 9] Bad file descriptor
PS F:\githouse\OMOOC2py\_src\om2py3w\3wex0>  '''