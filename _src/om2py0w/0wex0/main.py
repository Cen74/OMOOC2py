print "This is Cen's interactive Diary System"

diary = open('Diary.txt', 'a+')

print "I will open the following file: %r" % diary.name


text = ""
stopword = "q"
print "Enter \'q\' to quit input"

while True:
	line = raw_input('input >')
	if line.strip() == stopword:
		break
	text += "%s\n" % line
	
diary.write(text)

diary.seek(0)

print_diary = "If you want to print diary, Enter \'y\'?"
mark = raw_input(print_diary)


if mark.lower() == 'y':
	print "The content of the diary is:"
	print diary.read()
else:
	print "quit the diary"
		
	
diary.close()