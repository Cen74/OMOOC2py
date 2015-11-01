# -*- coding: UTF-8 -*-
from socket import*  
  
HOST='localhost'  
PORT=8080  
BUFSIZ=1024  
ADDR=(HOST,PORT)  
  
udpCliSock=socket(AF_INET,SOCK_DGRAM) #SOCK_DGRAM表示UDP通信  
  
while True:  
    data=raw_input('> ').encode('utf8')  
    if not data:  
        break;  
    udpCliSock.sendto(data,ADDR)  
    (data,ADDR)=udpCliSock.recvfrom(BUFSIZ) #可以得到ADDR  
    #if not data:  
    #    break;  
    print(data.decode('utf8'))  
  
udpCliSock.close()  