# -*- coding: utf-8 -*-
from datetime import date

print "This is Cen's interactive Diary System"

diary = open('Diary.txt', 'a+')

print "I will open the following file: %r" % diary.name

text = ""
stopword = "q"
print "Enter \'q\' to quit input"
# now = date.todayf

while True:
	line = raw_input('input >')
	if line.strip() == stopword:
		break
	text += "%s\n" % line
	
diary.write(text)

# 将文件指针启示设置为0
diary.seek(0)

print_diary = "If you want to print diary, Enter \'y\'?"
mark = raw_input(print_diary)


if mark.lower() == 'y':
	print "The content of the diary is:"
	print diary.read()
else:
	print "quit the diary"
		
	
diary.close()