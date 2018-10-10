import socket

'''
socket 通信
客户端
'''

# 创建一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 项服务端发起请求，参数是一个两个元素的元组，地址和端口
client.connect(("192.169.30.183", 8081))

count = 0

# 持续发送和接收数据
while True:

    count += 1

    data = input("客户端说：\n")

    # 发送数据，需要编码
    client.send(data.encode("utf-8"))

    # 接收数据，进行解码
    info = client.recv(1024).decode("utf-8")
    print("服务器说：", info)
