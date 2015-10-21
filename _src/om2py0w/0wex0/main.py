print "This is Cen's interactive Diary System"

diary = open('Diary.txt', 'a+')

print "I will open the following file: %r" % diary.name


text = ""
stopword = ""
while True:
	line = raw_input('input >')
	if line.strip() == stopword:
		break
	text += "%s\n" % line
	
diary.write(text)

diary.seek(0)

print_diary = "Do you want to print the diary. Y/N?"
mark = raw_input(print_diary)

if mark == 'Y':
	print "The content of the diary is:"
	print diary.read()
else:
	print "quit the diary"
		
	
diary.close()