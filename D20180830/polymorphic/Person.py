from polymorphic.Cat import Cat
from polymorphic.Mouse import Mouse

class Person:

    # 定义喂食方法，具体给哪种动物喂食并不关心
    # 只要知道给动物喂食就行了
    # 多态
    # Python是个动态类型语言，在多态的表现上没那么强烈与具体，
    # 只在继承关系上表现出多态，
    # 一个变量被赋值什么对象，它就是什么对象类型，而没有类似java中的子类对象赋值给父类类型的表现，
    def feedAnimal(self,animal,food):

        print("给"+animal.name+"喂"+food)
        animal.eat(food)



if __name__ == "__main__":

    p1 = Person()

    tom = Cat("tom")
    jerry = Mouse("jerry")

    # 将Animal的子类对象传入，执行喂食
    p1.feedAnimal(tom, "fish")
    p1.feedAnimal(jerry, "rice")