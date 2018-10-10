

def sayGood():
    print("good")

def sayHello():
    print("hello")

'''
 __name__ 属性指示调用当前模块的主体，如果是模块脚本自身执行，则值为"__main__"，即主函数调用，
 如果是通过其他程序引入该模块，则值为当前模块的名称，即cuixd
'''

# 判断，只有在本模块自身执行时才输出"这是cuixd.py文件"，否则不输出
if __name__ == "__main__":
    print(__name__)
    print("这是cuixd.py文件")
else:
    print(__name__)