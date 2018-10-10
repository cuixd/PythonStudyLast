# 字典类型练习
score = {"cuixd":70, "lilj":80}

# 取值
# 中括号取值如果key不存在会报错
print(score["cuixd"])

# get 取值 key不存在返回None
print(score.get("cuixd"))
print(score.get("cuixd1"))

# 插入
score["songf"] = 90

# 删除
score.pop("cuixd")


# 字典的遍历
# key的遍历
print("\nkey的遍历")
for k in score:
    print("%s : %d" % (k, score[k]))

# value的遍历
print("\nvalue的遍历")
for v in score.values():
    print(v)

# key-value 键值对元组遍历
print("\nkey-value 键值对元组遍历")
for  kv in score.items():
    print(kv)

# 枚举器遍历，可对keys或values进行枚举遍历，前面的序号只是获取的行号，并不代表
# 字典中的实际顺序
print("\n枚举器遍历")
for i, k in enumerate(score):
    print(i, k)

for i, v in enumerate(score.values()):
    print(i, v)

s1 = { 1,3,5,"7","cuixd"}

print(s1)