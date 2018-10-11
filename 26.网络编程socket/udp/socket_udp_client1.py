import socket

'''
utp通信 客户端
'''
# 创建一个udp socket对象，即完成客户端创建
udpclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 持续接收
while True:

    clisend = input("client1:")
    # 想服务端发送信息 sendto方法，信息内容需要编码和服务端地址元组(ip，端口)
    udpclient.sendto(clisend.encode("utf-8"),("192.169.30.183", 8082))
    # 接收来自服务端的信息，返回信息内容和地址元组
    recvdata, addr = udpclient.recvfrom(1024)
    # 打印接收到的信息
    print(addr, ":", recvdata.decode("utf-8"))

