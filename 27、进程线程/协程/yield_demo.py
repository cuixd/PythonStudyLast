

'''
    协程
    yield n 控制函数阶段执行
'''


def A():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30


m = A()

print(next(m))

print(next(m))

print(next(m))