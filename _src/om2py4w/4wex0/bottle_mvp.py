#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bottle import route, run, template, request, get, post

"""
@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)




@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

"""

@get('/diary')
def welcome():
	return '''
        <form action="/diary" method="post">
            输入: <input name="content" type="text" />
            value:<input type="text" size="44" name="t1" value="文本内容">
            <input value="确认" type="submit" />
        </form>
    '''
@post('/diary')
def print_input():
	content = request.forms.get('content')
	return "you input is %s" % content

run(host='localhost', port=8088, debug=True,reloader=True)



