#!usr/bin/python
#encoding=utf-8
import socket

def do_handle(clientsoc):
    while True:
        text = clientsoc.recv(1024)
        print text,"字节数：",len(text)
        if text == "end" or text == "":
            print "client close..."
            break
        clientsoc.send(text)#回显给客户端
    clientsoc.close()#关闭客户端
    print "客户端已关闭..."
    
    
#搭建Python服务器
'''
1、创建套接字  socket
2、绑定        bind
3、监听        listen
4、接收        accept
5、通信        send/recv
'''
#创建套接字
serversoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#设置套接字选项，解决地址重复绑定问题
serversoc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#绑定主机地址
'''
hostname = "raspberrypi.local"
hostIP = socket.gethostbyname(hostname)
hostPort = 8800
serversoc.bind(hostIP, hostPort)
'''
serversoc.bind(("127.0.0.1",8800))
#监听
serversoc.listen(5)
#接收
try:
    while True:
        clientsoc,addr = serversoc.accept()
        print clientsoc,addr
        do_handle(clientsoc)#数据读写
except KeyboardInterrupt:
    pass
    
    

    
    