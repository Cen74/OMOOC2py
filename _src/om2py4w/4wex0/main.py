# -*- coding: UTF-8 -*-
from datetime import datetime
import sys
import os
from bottle import route, run, template, request, get, post, view

def diary_lines():
    diary = open('diary.txt')
    content = diary.readlines()
    content = content
    diary.close()
    return content 

def check_file():
    if os.path.exists('diary.txt'):
        file_content = diary_lines()
    else:
        file_content = "Empty Diary" 

    return file_content


def diary_write(data):  
    with open('diary.txt', 'a+') as diary:
        wtime = datetime.now()
        diary.write(wtime.strftime("%Y/%m/%d %H:%M:%S ")+ data) 
        diary.write('\n')

print check_file() 


@get('/diary')
def welcome():
	data = check_file()
	return template('welcome_diary', content=data )


@post('/diary')
def print_input():
    client_input = request.forms.get('content')
    diary_write(client_input)
    data = diary_lines()
    return template('welcome_diary', content=data)
        	
       
run(host='localhost', port=8080, debug=True,reloader=True)








