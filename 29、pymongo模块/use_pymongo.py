from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
'''
python3 连接mongodb的模块 pymongo
在增删改查写法上与mongodb的命令基本一致，
只在{options} 指定选项true或者false时有区别，如upsert multi 等

ObjectId 是用于通过_id来进行查询时生成_id的对象
'''

# 创建连接
conn = MongoClient("10.211.55.55", 27017)

# 连接的权限认证登录
conn["admin"].authenticate("root", "mongodb")

# 获取数据库
db = conn["mydb"]

# 获取集合
collection = db["emp"]

# 插入
collection.insert({"empno":1007, "ename":"李雷", "age":23, "job":"edu", "gender":"male"})

# 更新, 注意对于options选项部分，mongodb的标准api是 使用{option:true|false}来表示的
# 但是，python中表示布尔类型是True或False，在表示这一块的时候，省略了{}，而且使用option=True|False的方式来指定
collection.update({"ename":"李雷"}, {"$set":{"age":25}}, upsert=False)

# 删除
collection.delete_one({"ename":"李雷"})

# 查找, 获得的结果是一个可迭代对象的游标，可以使用循环遍历，每一个遍历对象是一个dict
res1 = collection.find({"ename":"李雷"})
print(type(res1))
for e in res1:
    print(e, type(e))

res2 = collection.find(
    {
          "$or":[
            {"job":"edu","age":{"$lt":30},"gender":"fmale"},
            {"job":"bank","age":{"$lt":30},"gender":"fmale"}
              ]
        }
)

for e in res2:
    print(e, type(e))

# 使用ObjectId生成_id进行指定查询
res3 = collection.find({"_id":ObjectId("5bc721ce1da2612835fed639")})
print(res3.next())

# 升序排序
print("@@@@@@@@@@@@@@@@@升序排序@@@@@@@@@@@@@@")
res4 = collection.find({}).sort("age")
for e in res4:
    print(e)

print("@@@@@@@@@@@@@@@@@降序排列@@@@@@@@@@@@@@")

res5 = collection.find({}).sort("age", pymongo.DESCENDING)
for e in res5:
    print(e)