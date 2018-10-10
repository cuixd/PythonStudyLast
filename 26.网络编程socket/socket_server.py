import socket

'''
socket 通信
服务端
'''
# 创建服务端socket
# AF_INET 设定ipv4
# SOCK_STREAM 指定以流的方式进行传输
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务端地址和端口，创建一个服务器，参数是一个两个元素的元组，地址和端口
server.bind(("192.169.30.183", 8081))

# 接受监听，5表示同时接受最多5个客户端的请求，目前形同虚设，待使用线程后体现
server.listen(5)
print("服务器启动成功....")

# 接受请求，返回两个值，一并接收，一个是客户端socket对象，一个是客户端地址
clientSocket, clientAddr = server.accept()
print("接收到来自(%s, %s)客户端的请求" %(str(clientSocket), clientAddr))

# 定义一个死循环持续接收数据
while True:

    # 接收来自客户端的数据，需要解码
    recvinfo = clientSocket.recv(1024).decode("utf-8")
    print(recvinfo)

    # 发送给客户端数据，需要编码
    clientSocket.send("地瓜地瓜，我是土豆".encode("utf-8"))