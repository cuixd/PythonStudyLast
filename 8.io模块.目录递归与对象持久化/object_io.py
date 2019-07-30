import pickle  # 对象持久化模块

# list  tuple  set dict的写入和读取
# o1 = [1, "cxd", "崔晓东"]
o1 = (1, "cxd", "崔晓东")
o1 = {1, "cxd", "崔晓东"}
o1 = {"id": 1, "name": "cuixd", "age": 33}
path = "/PycharmProjects/PythonStudy/8.io模块.目录递归与对象持久化/object.txt"
f1 = open(path, "wb")

# 将对象dump到文件中
pickle.dump(o1, f1)
f1.close()

# 以二进制读取方式打开文件
with open(path, "rb") as f2:
    # 将文件内容加载
    l1 = pickle.load(f2)
    print(l1)
    print(type(l1))

# 如果对象是一个dict，则执行遍历
if isinstance(l1, dict):
    # 使用enumerate枚举，返回的是一个(序号,元素)的元组tuple
    for k in enumerate(l1.keys()):
        print(k)
        print(k[1], l1.get(k[1]))

    # 遍历key,由key获取value
    for k in l1.keys():
        print(k, l1.get(k))
