import socket

'''
udp通信 服务端
udp是面向无连接的，非安全的通信，不需要建立连接，自由的进行发送和接收
'''

# 创建udp socket通信，通过指定socket.SOCK_DGRAM标识udp
udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定一个地址和端口，开启服务
udpserver.bind(("192.169.30.183", 8082))

# 持续接收
while True:

    # revcfrom方法，返回接收到的数据和客户端地址，地址是一个元组(ip,port)
    recvinfo, addr = udpserver.recvfrom(1024)
    # 打印接收信息，需要解码
    print(addr,":",recvinfo.decode("utf-8"))
    # 回复客户端 sendto方法，指定信息，和客户端地址
    udpserver.sendto((str(addr) + "你的信息，我已收到").encode("utf-8"), addr)