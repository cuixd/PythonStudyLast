import os

# for a in ["1","2","3"]:
#
#     locals()["v"+a] = a
#     print(locals()["v"+a])

path="/usr/local/aaa.txt"

res = os.path.splitext(path)

print(res)


res = os.path.basename(path)

print(res)

list1 = [[1,2,3],[4,5,6],[7,8,9]]

for rowdata in list1:
    print(rowdata)