import datetime

'''
datetime模块中的类：
datetime 日期时间
datedelta 时间跨度
tzinfo 时区信息
time 时间
date 日期

最常用的是datetime
'''
#获取当前日期时间，默认就是 YYYY-mm-dd HH:MI:SS.xxxxxx 格式
t1 = datetime.datetime.now()
print(t1,type(t1))

# 以datetime类的构造方法生成一个datetime对象，参数列表就是年、月、日、时、分、秒、6位微秒
t2 = datetime.datetime(2018,8,27,17,54,55,123456)
print(t2, type(t2))

# 日期时间对象转换为字符串
t3 = t2.strftime("%Y-%m-%d %X")
print(t3, type(t3))

# 将日期时间字符串转换为datetime对象，字符串的实际格式要与指定的格式模式匹配
t4 = datetime.datetime.strptime(t3,"%Y-%m-%d %H:%M:%S")
print(t4, type(t4))


t5 = datetime.datetime.now()
t6 = datetime.datetime(1985,1,1,10,22,54,123456)

# datetime类型相减，获得相差的天数、小时 分钟 秒 微秒
t7 = t5 - t6
print(t7)

#提取差额的天数、天数以外的时分秒转换后的秒数
print(t7.days,t7.seconds)
