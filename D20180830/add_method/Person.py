from types import MethodType # 为实例添加方法需要用到

class Person:

    # 特殊参数，限制类的实例允许被定义的属性或方法
    __slots__ = ("name", "age", "speak")

    def __init__(self, name):

        self.name = name

        # aaa属性不被允许，因为__slots__限制
        # self.aaa = "aaa"


if __name__ == "__main__":

    p1 = Person("cuixd")

    # 为实例添加age属性
    p1.age = 33

    print(p1.name, p1.age)

    # 定义一个方法
    def say(p):

        print(p.name + " is speaking")

    # 通过MethodType方法为实例添加speak方法
    p1.speak = MethodType(say, p1)

    p1.speak()


    # 以下属性和方法不能被添加，因为__slots__属性限制了
    # height 属性不允许添加
    # p1.height = 70

    # say方法不允许添加
    # p1.say = MethodType(say, p1)


