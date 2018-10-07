
'''
filter(func, iter)
过滤器函数，类似map函数的处理逻辑，将iter可迭代对象的每一个元素进行func的逻辑处理，
处理的结果返回True则保留该元素，否则舍弃该元素，最终返回一个过滤后的迭代对象

'''

def getEven(num):


    if int(num)%2 == 0:
        return True
    return False

str1 = '18258459959'

res = filter(getEven,str1)

print(''.join(list(res)))
