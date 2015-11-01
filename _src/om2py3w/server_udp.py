# -*- coding: UTF-8 -*-
from socket import *  
from time import ctime  
  
HOST=''  
PORT=8080  
BUFSIZ=1024  
ADDR=(HOST,PORT)  
  
udpSerSock=socket(AF_INET,SOCK_DGRAM) #SOCK_DGRAM表示是UDP通信  
udpSerSock.bind(ADDR) #绑定到ADDR，由于没有'虚电路'，无连接，所以不需要listen，只是被动等待数据到来  
  
while True: #被动等待数据到来  
    print('waiting for message...')  
    (data,addr)=udpSerSock.recvfrom(BUFSIZ) #当有数据到来时，得到data与源addr。注意这里不能产生一个新的socket，因为UDP是无连接的  
    data=data.decode('utf8') #bytes转换成utf-8  
    udpSerSock.sendto(('[%s] %s'%(ctime(),data)).encode('utf8'),addr) #传输处理后的数据，需要写addr，仍然因为是无连接  
    print('...received from and returned to:',addr)  
  
udpSerSock.close()  