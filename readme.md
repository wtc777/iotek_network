#iotek_network
基于TCP/UDP协议的客户端服务器端搭建代码

TCP协议：
  建立链接时：三次握手；断开连接时：四次挥手断开客户端服务器端套接字的读写通道
  服务器端搭建
    1、创建套接字
    2、绑定IP地址和端口号
    3、listen监听
    4、accept接收来自客户端的链接
    5、write/send 数据包读写
    6、close关闭套接字
  客户端搭建
    1、创建套接字
    2、connection链接服务器
    3、write/send 数据包读写
    4、close 关闭套接字
c++实现

c++_QT实现

Python实现

