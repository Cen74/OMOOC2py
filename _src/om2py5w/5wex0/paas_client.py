 # -*- coding: UTF-8 -*-  
import requests
import sys
import os 


'''
def print_html(data):
	content = BeautifulSoup(data, "html.parser")
	for line in content.find_all('br'):
		print line.get_text()
'''

def foo():


	login = requests.get('http://localhost:8080/cmd')

	print login.text
	print '-'*10


	TAG = 'Null'

	while True:
		input_c = raw_input('%s>' % TAG)

		print input_c[0:3]
		if input_c in ['help', 'h', '?']:
			print """
			   \'q\' or \'quit\' \'bye\' for help
 
			   \'h\' or \'help\' or \'bye\' to exit

			   syn to return history

			   st:TAG to set tags

			   ls: list TAGs 

			   FLUSH to clear diary

			  """
		elif input_c in ['bye', 'q' ,'quit']:
			print "bye"
			break
		
		elif input_c == 'syn':
			history = requests.get('http://localhost:8080/diary')
			print "The diary histroy is :", '-'*10
			print_html(history.text)
		
		elif input_c[0:3] == 'st:':
			TAG = input_c[3:]
			print TAG
			if TAG != []:  # is not [] 不起作用
				print 'not Null'
				set_TAG = requests.post("http://localhost:8080/cmd/set", data = {"key":TAG})
				print set_TAG.text

			else:
				TAG = 'Null'
				print 'finsish'

			

		else:
			requests.post("http://localhost:8080/cmd", data = {"key":input_c})



if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()


