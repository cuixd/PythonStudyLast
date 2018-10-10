
'''
打开一个文件open方法
open(path,mode,encoding=)
path 文件的绝对路径
mode 打开文件的方式:
    r   只读打开
    rb  二进制只读打开
    w   写打开
    wb  二进制写打开
    a   追加方式打开
encoding=   指定以哪种字符集打开，因该参数并不是参数列表的第三个参数，
    所以要以k=v形式指定
'''
f1 = open("/PycharmProjects/PythonStudy/6.函数.装饰器.偏函数.异常与文件读取/info.txt", 'r', encoding='utf8')

# read()读取整个文件
# content = f1.read()
# print(content)

'''
 seek(n) 调整文件指针的位置，文件的读写是以流的方式进行的，当前一个read()读完后
指针到了结束位置，要想重新读取，就要调整指针的位置
'''
# 调整指针到开头
f1.seek(0)

# read(n)读取n个字符
str1 = f1.read(11)
# str2= f1.read(10)

print("str1=",  str1)

# readline() 按行读取，读取一行
print("按行读取")
line = f1.readline()
print(line)
line = f1.readline()
print(line)


# readlines() 将文件以行全部读取，存放在list中，每行作为list的一个元素
f1.seek(0)
linelist = f1.readlines()
print(linelist)

# 文件每次打开后应该及时关闭
if not f1.closed:
    f1.close()

print(f1.closed)

# 以with as方式打开并命名一个文件流，操作完成后会自动关闭
with open("/PycharmProjects/PythonStudy/6.函数.装饰器.偏函数.异常与文件读取/info.txt", 'r', encoding='utf8') as f2:
    print(f2.read())

print(f2.closed)
