# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
from datetime import datetime

import sys
import os 

def diary_history():
    diary = open('diary.txt')
    content = diary.read()
    content = content
    diary.close()
    return content #传递unicode的字符串


def diary_write(data, addr):  
    with open('diary.txt', 'a+') as diary:
        wtime = datetime.now()
        diary.write(wtime.strftime("%Y/%m/%d %H:%M:%S")+' client['+
            str(addr[1])+']   '+ data)  # 传递端口号
        diary.write('\n')

def setup_udp_server(HOST='', PORT=4444):
    HOST = ''
    PORT = 4444

    ADDR=(HOST,PORT) 

    diary_server = socket(AF_INET, SOCK_DGRAM)
    diary_server.bind(ADDR)

    return diary_server

def check_file():
    if os.path.exists('diary.txt'):
        file_content = diary_history()
    else:
        file_content = "Empty Diary" 

    return file_content



def diary_udp_server(): #可以里面的变量重名
    
    diary_server = setup_udp_server()

    BUFSIZ=1024

    file_content = check_file()
   

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
            diary_write(data, addr_client)

    diary_server.close()


if __name__  == '__main__':
    if 1 != len(sys.argv) :
        print ''' Usage: $python main.py '''
    else:
        diary_udp_server()