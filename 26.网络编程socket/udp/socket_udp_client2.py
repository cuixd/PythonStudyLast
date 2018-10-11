import socket

udpclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    clisend = input("client2:")
    udpclient.sendto(clisend.encode("utf-8"),("192.169.30.183", 8082))
    recvinfo, addr = udpclient.recvfrom(1024)
    print(addr, ":", recvinfo.decode("utf-8"))

