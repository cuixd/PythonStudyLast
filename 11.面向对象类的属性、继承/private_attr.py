class Person:

    def __init__(self,name,age,money):
        self.name = name
        self.age = age

        # 属性前加__双下划线，则是一个私有属性，类的外部无法通过实例名.私有属性的方式获取值
        self.__money = money


    def __str__(self):

        # 在类的方法内部可以直接获取私有属性的值
        return "My name is %s,I am %d years old, I hava %d yuan" %(self.name, self.age, self.__money)

    '''
    成员属性的get set方法
    '''

    def eat(self, food):

        print(self.name + "吃" + food)

    def getMoney(self):

        return self.__money

    def setMoney(self,money):

        if money < 0:
            money = 0
        self.__money = money

    '''
    私有属性的另一种访问方式，这种方式可以允许通过实例变量名.属性的方式直接获取和设置属性
    '''

    # 定义与私有属性同名(舍去双下划线)的方法，结合@property提示(装饰器)，来实现get方法
    @property
    def money(self):

        return self.__money

    # 定义私有属性同名(舍去双下划线)带参方法，结合@属性.setter提示来实现set方法
    @money.setter
    def money(self, money):

        if money < 0:
            money = 0
        self.__money = money


if __name__ == "__main__":
    p1 = Person("cuixd",33,200)

    print('f', p1)

    # 类的外部无法通过实例名.私有属性的方式获取值，也就是无法获取该变量，pycharm甚至都没有提示该属性
    # print(p1.__money)

    # 而这里可以赋值和获取值，是因为python是解释型动态语言，
    # 可以动态的为对象添加属性，这里的__money并不是构造方法中的那个私有属性
    p1.__money = 10
    print(p1.__money)

    # 再次打印对象的信息，可以发现对象的私有属性__money依然是200
    print('a', p1)

    # 只能通过set方法修改私有属性的值
    p1.setMoney(10)
    print('x', p1)

    # 私有成员属性被Python解释器改名为, _类名__属性名，如下方式还是可以直接访问到私有属性并可以直接修改，不建议使用
    print(p1._Person__money)

    # 使用实例.属性(舍去双下划线)的方式访问和设置私有属性
    print('y', p1.money)
    p1.money = -100
    print('z', p1.money)
