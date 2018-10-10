import json

'''
json模块的功能
    加载：字符串（str类型或文件）转换为字典对象
        1、将json格式的字符串类型转换成dict类型  loads方法，表示内存间的加载转换流，
        2、将json格式的文件加载为dict类型   load方法，表示从文件加载到内存
    导出：将字典对象导出为字符串（str类型或文件）
        3、将dict类型转换为json格式字符串   dumps方法，表示内存间的转换流，s应该是stream的意思，方便区分和记忆
        4、将dict类型写出到json格式的文件   dump方法，将字典类型导出为文件，那么自然就是json格式了，其实也可以说是字典格式
'''
# 定义一个json格式的字符串
infojson = '''{"name":"cuixd",
           "age":"18",
           "info":{"city":"hangzhou",
                   "work":"dba",
                   "hoby":["王者荣耀","绝地求生"]
                   }
           }'''

# 将字符串加载为字典，方便读取信息
infodict = json.loads(infojson)
print(infodict)
print(type(infodict))

# 例如，通过字典api 以及数组下标选取到第一个爱好
print(infodict.get("info").get("hoby")[0])

# 将字典转换为字符串，ensure_ascii=False 表示允许有非ascii字符，也就是允许中文，默认是True
# 这样在转换为字符串后，中文便可正常显示，而不是一串unicode码
jsonstr = json.dumps(infodict, ensure_ascii=False)
print(jsonstr)
print(type(jsonstr))

# 将字典类型导出到文件，定义一个文件写入流
with open("/Users/cuixiaodong/PycharmProjects/PythonStudy/25.网络爬虫urllib模块三/info.json", "w") as f:
    # 进行导出，同样要指定ensure_ascii=False，
    json.dump(infodict, f, ensure_ascii=False)

# 将一个json文件加载到内存为字典类型
with open("/Users/cuixiaodong/PycharmProjects/PythonStudy/25.网络爬虫urllib模块三/info.json", "rb") as f:
    data = json.load(f)
    print(data)