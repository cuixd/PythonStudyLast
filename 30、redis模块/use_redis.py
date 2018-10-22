import redis

'''
python与redis的交互模块
'''

# db=1指定连接redis的哪个db，decode_responses对返回结果进行解码，用于正确显示中文，否则显示的是unicode码
conn = redis.StrictRedis("10.211.55.55", port=6379, password="redis",db=1, decode_responses=True)


# 根据数据结构类型的不同，使用对应的方法
conn.set("name", "cuixd")
name = conn.get("name")
print(name)

listres = conn.lrange("game", 1, -1)
print(type(listres), listres)

hashitemres = conn.hget("info", "name")
print(hashitemres)

hashdictres = conn.hgetall("info")
print(type(hashdictres), hashdictres)

setres = conn.smembers("emp")
print(type(setres), setres)


# 使用pipline进行批量提交，对于写请求，直接使用连接去调用单个命令，由于是多个独立的请求，会消耗请求资源
# 使用pipline来编写多条命令，最后进行一次性执行

pl = conn.pipeline()
pl.set("s1", "a")
pl.set("s2", "b")
pl.set("s3", "c")
pl.set("s4", "d")

pl.execute()


