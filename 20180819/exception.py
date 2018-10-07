# python 异常处理格式
# 1
'''
try:
    代码
except 错误码1 as e:
    错误处理代码1
except 错误码2 as e:
    错误处理代码2
......
else:
    没有出现异常是才执行的代码
'''

try:
    print(num)
except NameError as e:
    print("没有这个变量啊", e)
else:
    print("没问题啊")

num = 1
try:
    print(num)
except NameError as e:
    print("没有这个变量啊", e)
else:
    print("没问题啊")

# 2  不明确指定捕获哪些异常，统一处理
'''
try:
    代码
except:
    错误处理代码
else:
    没有出现异常是才执行的代码
'''

# 3  一次捕获多个异常
'''
try:
    代码
except (错误码1, 错误码2):
    错误处理代码
else:
    没有出现异常是才执行的代码
'''

# 如果异常没有被成功捕获，那么害死会报错，下面这个例子只对变量未定义的异常进行了捕获
# 因此，数组下标越界的错误还是会报错，从而程序终止
try:
    list = [1, 2, 3]
    print(list[3])
except NameError as e:
    print(e)
else:
    print("正常啊")


print("看来我是打印不出来了")

# finally
'''
try:
    代码
except 错误码1 as e:
    错误处理代码1
except 错误码2 as e:
    错误处理代码2
......
finally:
    始终要执行的的代码
'''