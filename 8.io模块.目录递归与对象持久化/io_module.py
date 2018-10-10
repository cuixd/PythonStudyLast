import os.path  #操作系统模块

# 获取操作系统的类型与详细信息
print(os.name)
print(os.uname())

# 获取环境变量
env = os.environ
print(type(env))
print(env)

# 环境变量可以认为是一个dict类型，可以进行遍历
for name in env.keys():
    print(name,env.get(name))

# 获取当前相对路径  其实就是 .
print(os.curdir)

# 获取绝对路径
print(os.getcwd())

# 获取路径下的全部文件，列表形式
dirlist = os.listdir("/Users/cuixiaodong/PycharmProjects/PythonStudy/8.io模块.目录递归与对象持久化")
print(type(dirlist))
print(dirlist)


# 当前目录已存在的话，创建会失败，但是无报错，所以之后的代码将不会执行
# 创建目录，当前目录下创建
os.mkdir("cuixd")
# 绝对路径下创建
os.mkdir("/Users/cuixiaodong/PycharmProjects/PythonStudy/cuixd")

# 删除目录，当前路径下
os.rmdir("cuixd")
# 删除目录，绝对路径
os.rmdir("/Users/cuixiaodong/PycharmProjects/PythonStudy/cuixd")

#级联创建目录
# os.makedirs("/Users/cuixiaodong/PycharmProjects/PythonStudy/8.io模块.目录递归与对象持久化/cuixd1/1/2")


#os.mkdir("test")

# 查看文件状态信息
#print(os.stat("test"))

# 执行系统命令
os.system("ls -l")

# 打开mac系统中的应用程序 网易云音乐
# os.system("open /Applications/NeteaseMusic.app")

# os.path下的获取当前路径的绝对路径
print(os.path.abspath("."))

# 拼接路径，第二个参数之后的都表示要拼接的部分
jp = os.path.join("/Users","cuixiaodong/Downloads","崔晓东")
print(jp)

subpath = "/Users/cuixiaodong/Downloads/崔晓东.txt"
# 拆分路径，将最后一级与前缀路径分割，获得一个元组
sp = os.path.split(subpath)
print(sp)

# 拆分文件名与扩展名，获得元组类型
print(os.path.splitext("崔晓东.txt"))

path1 = "/Users/cuixiaodong/PycharmProjects/PythonStudy/8.io模块.目录递归与对象持久化"
# 判断是否是目录或者文件
print(os.path.isdir(path1))
print(os.path.isfile(path1))

# 判断目录或文件是否存在
print(os.path.exists(path1))

# 获取文件的大小，单位是字节
path2 = "/Users/cuixiaodong/PycharmProjects/PythonStudy/8.io模块.目录递归与对象持久化/object_io.py"
print(os.path.getsize(path2))

# 获取文件的目录及文件名
print(os.path.dirname(path2))
print(os.path.basename(path2))

#os.makedirs("/Users/cuixiaodong/PycharmProjects/PythonStudy/8.io模块.目录递归与对象持久化/1/2/3")

# 递归列出目录
def list_dir(dir,level):
    if os.path.exists(dir):
        print("****" * level+dir)
        if os.path.isdir(dir):
            level += 1
            dirlist = os.listdir(dir)
            for file in dirlist:
                absfile = os.path.join(dir,file)

                list_dir(absfile,level)

    else:
        print(dir,":Directory or file is not exist")

list_dir("/Users/cuixiaodong/PycharmProjects/PythonStudy/8.io模块.目录递归与对象持久化",0)


# 递归求和1+2+3+。。。N
def getsum(n):
    if n > 1:
        return n + getsum(n - 1)
    else:
        return n

print(getsum(1))