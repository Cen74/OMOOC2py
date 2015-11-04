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
	diary_client.sendto('test', ADDR)
	(feedback, addr) = diary_client.recvfrom(BUFSIZ)
	print addr 
	print feedback.decode('UTF-8')

	while True:
		input_c = raw_input(' > ')

		if input_c == 'help' or input_c == 'h' or input_c == '?':
			print """
			  press \'q\' or \'quit\' \'bye\' for help
 
			  press  \'h\' or \'help\' or \'bye\' to exit

			  press syn to return history"""
		elif input_c == 'bye' or input_c == 'q' or input_c == 'quit':
			print "bye"
			break
		elif input_c == 'syn':
			diary_client.sendto('syn', ADDR)
			history = diary_client.recv(BUFSIZ)
			print history.decode('UTF-8') # utf-8 object
		else:
			data = input_c.decode('gb2312').encode('UTF-8') #windows下中文编码方式为gb2312
			diary_client.sendto(data, ADDR)
			#(recv, addr) = diary_client.recvfrom(BUFSIZ)

			#print "recv: \n %r , from %r " % (recv.decode('UTF-8'), addr)
		
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