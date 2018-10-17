import pymysql

'''
PyMySQL是python3连接MySQL常用的模块

'''

# 创建一个连接
db = pymysql.connect("10.211.55.53", "root", "oracle", "hr")

# 打开一个游标
cursor = db.cursor()

# mysql的命令行管理sql也可以执行
sql1 = "show tables"

# 游标执行语句
cursor.execute(sql1)

# 获取游标数据
data = cursor.fetchall()

# 数据是类型是一个元组，如果是多行结果，是一个二维元组，如果是单行，则是一个一维元组
print(data, type(data))

# 删除表语句 if exists，如果表不存在，会给出错误提示，但是不会中断程序往下执行
sql2 = "drop table if exists python"

# 经过测试，即使表不存在，进行如上if exists的判断删除，不会进入异常代码的捕捉
# 也就是说，控制台虽然给出表不存在的错误提示，但是python解释器并不认为这是异常
try:
    cursor.execute(sql2)
except:
    print("删除未成功，可能不存在该表")

# 建表
sql3 = "create table python(id int primary key, version varchar(10))"

try:
    cursor.execute(sql3)
    print("创建表成功")

except:
    print("创建表出错")

# insert
sql4 = "insert into python values(1, '3.6'), (2, '2.7.2')"

# 增删改操作，要加异常捕获，并且需要进行提交，不论数据库是否设置了自动提交
# python的数据库连接都不会自动提交事务，必须进行db.commit()
try:
    cursor.execute(sql4)
    db.commit()
except:
    print("插入数据失败")

# update
sql5 = "update python set version='3.6.5' where id = 1"

try:
    cursor.execute(sql5)
    db.commit()
except:
    print("更新数据失败")

# delete
sql6 = "delete from python where id = 2"

# 如果不进行commit,删除只在当前会话生效，删除的数据不再可见，但是实际并未提交而没有被删除，其他会话依然可见
try:
    cursor.execute(sql6)
    #db.commit()
except:
    print("删除数据失败")

sql7 = "select * from python"
cursor.execute(sql7)
# 获取全部行
data = cursor.fetchall()
# 结果是个二维元组
print(data)
print(data[0])

cursor.execute(sql7)
# 获取一行
data = cursor.fetchone()
# 一维元组
print(data)

cursor.close()

db.close()