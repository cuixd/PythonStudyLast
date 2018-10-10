from private_attr import Person


class Student(Person):

    def __init__(self,id,name,age,money):

        # 继承父类构造方法的3种写法：
        # 1、super()引用父类
        super().__init__(name,age,money)
        # 2、super(Student,self)指定子类名称，表示将当前Student的self对象传给父类
        # super(Student,self).__init__(name,age,money)
        # 3、显式指定父类，构造方法中要有self，表示将子类对象传给父类的构造方法，
        # 这种写法多用于多继承子类的构造方法，多继承时也只能用这种显式写法
        # Person.__init__(self,name,age,money)

        # 子类特有的属性
        self.id = id

    # 子类的独有方法
    def study(self):
        print(self.name + "正在学习")

    # 重写父类的__str__方法，舍去money信息，增加id信息
    def __str__(self):

        # 父类的私有属性无法继承
        # print(super.__money)
        return "My name is %s,I am %d years old, My id is %d " %(self.name, self.age, self.id)


stu1 = Student(1,"cuixd",33,100)
stu1.study()
print(stu1)

# 因为父类的money属性为私有，只能通过get方法获取
print(stu1.getMoney())

# print(stu1.__money)
