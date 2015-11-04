# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import date
import sys
import os 

def diary_history():
    diary = open('diary.txt')
    content = diary.read()
    content = content.decode('UTF-8').encode('UTF-8')  
    diary.close()
    return content #传递unicode的字符串

def foo():
    HOST = ''
    PORT = 4444
    BUFSIZ=1024  
    ADDR=(HOST,PORT) 

    diary_server = socket(AF_INET, SOCK_DGRAM)
    diary_server.bind(ADDR)

    if os.path.exists('diary.txt'):
        file_content = diary_history()
    else:
        file_content = "Empty Diary" 



    diary = open('diary.txt', 'a+', 0) #with statemanet / flush

    while True:
        print "waiting for connection"
        (data, addr_client) = diary_server.recvfrom(BUFSIZ)
        print "conncetd from %r, message: %r" % (addr_client, data)

        if data == 'test': 
            diary_server.sendto(file_content, addr_client)
    
        elif data == 'syn': # 在win power shell 
            #print type(content) 
            diary_server.sendto(diary_history(), addr_client)
        else:
            # print data 如果是中文，传递回来的不能正常显示 
            diary.write(data)
            diary.write('\n')

    diary.close()
    diary_server.close()


if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        foo()