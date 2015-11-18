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
			history = requests.post('http://localhost:8080/cmd/history', data = {"key":TAG})	
			print history.text
		
		elif input_c[0:3] == 'st:':
			TAG = input_c[3:]
			if TAG != '':   # is not None 不起作用
				set_TAG = requests.post("http://localhost:8080/cmd/set", data = {"key":TAG})
				print set_TAG.text
			else:
				TAG = 'Null'

		else:
			diary_line = {'key':TAG, 'value':input_c}
			record = requests.post("http://localhost:8080/cmd/input", data = diary_line)
			print record.text


if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()


