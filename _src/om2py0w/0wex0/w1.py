# -*- coding: utf-8 -*-
from datetime import date
import sys
import os 	
#  根据大妈演示修改

def print_diary():
    file_mark = os.path.exists("./Diary.txt")
    if file_mark == True:
	    print open('Diary.txt').read()
	    

def write_diary():
    diary = open('Diary.txt', 'a+')
    # help = ['help' 'h' '?']
    # quit = ['quit' 'q' 'bye'] 

    while True:
        input = raw_input(' > ')
        if input == 'help' or input == 'h' or input == '?':
            print """press \'q\' or \'quit\' \'bye\' for help
 
press  \'h\' or \'help\' or \'bye\' to exit"""
        elif input == 'bye' or input == 'q' or input == 'quit':
             diary.close()
             print "quit the diary"
             break
        else:
            diary.write(input)
            diary.write('\n')
      

def foo():
    print "This is Cen's interactive Diary System"
    print_diary()    
    write_diary()
    
   
if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()

"""
diary = open('Diary.txt', 'a+')

print "I will open the following file: %r" % diary.name

text = ""
stopword = "q"
print "Enter \'q\' to quit input"
now = date.todayf

while True:
	line = raw_input('input >')
	if line.strip() == stopword:
		break
	text += "%s\n" % line
	
diary.write(text)

＃将文件指针启示设置为0
diary.seek(0)

print_diary = "If you want to print diary, Enter \'y\'?"
mark = raw_input(print_diary)


if mark.lower() == 'y':
	print "The content of the diary is:"
	print diary.read()
else:
	print "quit the diary"
		
	
diary.close()
"""