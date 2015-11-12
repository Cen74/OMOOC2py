# -*- coding: UTF-8 -*-  
import requests
import sys
import os 
from bs4 import BeautifulSoup

def print_html(data):
	content = BeautifulSoup(data, "html.parser")
	for line in content.find_all('br'):
		print line.get_text()


def foo():
	print """
		press \'q\' or \'quit\' \'bye\' for help
 
		press  \'h\' or \'help\' or \'bye\' to exit

		press syn to return history"""

	login = requests.get('http://localhost:8080/diary')

	print '-'*10
	print_html(login.text)


	while True:
		input_c = raw_input(' > ')

		if input_c in ['help', 'h', '?']:
			print """
			  press \'q\' or \'quit\' \'bye\' for help
 
			  press  \'h\' or \'help\' or \'bye\' to exit

			  press syn to return history"""
		elif input_c in ['bye', 'q' ,'quit']:
			print "bye"
			break
		elif input_c == 'syn':
			history = requests.get('http://localhost:8080/diary')
			print "The diary histroy is :", '-'*10
			print_html(history.text)

		else:
			send = input_c.decode('gb2312').encode('UTF-8') #windows下中文编码方式为gb2312
			requests.post("http://localhost:8080/diary", data = {"content":send})



if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()


