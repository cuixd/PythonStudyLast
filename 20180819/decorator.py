import functools
# 装饰器的作用时将原本的函数进行修改，并返回一个新的函数

# 编写一个装饰器处理age为负数时便为0
def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner

# @装饰器名称 放在一个函数定义的上一行，表示用这个装饰器对下面的函数进行装饰
# 装饰后的函数名与原函数相同，这样就避免了手动的进行装饰器的调用来返回新函数
@outer
def speak(age):
    print("cuixd is %d years old."  %(age))

# truepeak = outer(speak)
#truepeak(-10)

speak(-10)

# 偏函数，修改某个函数的参数，将某些参数设为默认值，形成一个新的函数
def int2(numstr):
    return int(numstr, base=2)

print(int2("111"))

#python提供了这样的功能，在 functiontools中有一个partial方法就是来做这个的，
#她将返回一个新的方法
int3 = functools.partial(int, base = 2)
print(int3("1011"))
