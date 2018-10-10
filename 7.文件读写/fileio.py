# 以w方式打开，进入覆盖写模式，此时的写入方式是以编码后的字符方式写入的
f1 = open("/Users/cuixiaodong/PycharmProjects/PythonStudy/7.文件读写/info.txt","w")
# 写入一行字符，我的系统是macOS，默认是utf8字符集
f1.write("My name is 崔晓东\n")
# flush方法将文件缓存刷新到磁盘，再次之前，文件中并看不到内容
f1.flush()
# 关闭文件时，也会刷新文件缓存到磁盘
f1.close()

# 以二进制追加方式打开文件，此时的写入方式是二进制字节的
with open("info.txt",'ab') as f2:
    # 因此，要写入字符串，需要将字符串进行编码，此处以gbk编码
    f2.write("我来自中国".encode("gbk"))

# 以二进制读方式打开文件
with open("info.txt","rb") as fr:

    # 读取第一行，是二进制方式的
    line1 = fr.readline()
    print(line1)
    print(type(line1))

    # 因其是utf8编码的，所以要将其以正确的编码格式来解码获得字符串
    ln1 = line1.decode("utf8")
    print(ln1)
    print(type(ln1))

    # 读取第二行
    line2 = fr.readline()
    print(line2)

    # 以gbk解码
    ln2 = line2.decode("gbk")
    print(ln2)

print(fr.closed)

# errors="ignore" 忽略解码错误，即不能正确解码也不报错，而是显示乱码
with open("info.txt","r",encoding="utf8",errors="ignore") as f3:
    line1 = f3.readline()
    print(line1)

    line2 = f3.readline()
    print(line2)

