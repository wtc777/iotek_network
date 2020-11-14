#!usr/bin/python
#encoding=utf-8
import socket

def do_handle(clientsoc):
    while True:        
        msg = raw_input("请输入发送内容:")
        clientsoc.send(msg)
        text = clientsoc.recv(1024)
        print text,"字节数：",len(text)
        if text == "end" or text == "":
            print "client close..."
            break 
            
#搭建Python客户端
'''
1、创建套接字  socket
2、连接服务器  connect
5、通信        send/recv
'''
#创建套接字
clientsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#与服务器套接字建立链接
clientsoc.connect(("127.0.0.1",8800))
#接收
try:
    while True:
        do_handle(clientsoc)#数据读写
except KeyboardInterrupt:
    pass
clientsoc.close()#关闭客户端    
print "客户端已关闭..."   

       
    
    
    