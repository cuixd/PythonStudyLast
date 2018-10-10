from mutil_extend.Father import  Father
from mutil_extend.Mother import Mather

class Child(Father,Mather):

    def __init__(self, surname, name, fname, facevalue, mname):

        Father.__init__(self,surname,fname)
        Mather.__init__(self,facevalue,mname)
        self.name = name


    def play(self):

        print("玩耍")

    def __str__(self):

        return "我姓%s,名%s,我的父亲叫%s%s,母亲叫%s" %(self.surname, self.name,
                                            self.surname, self.getFname(), self.getMname())

if __name__ == "__main__":

    c1 = Child("张", "无忌", "翠山", 95, "殷素素")
    c1.play()
    c1.wash()
    c1.makeMoney()

    # 继承自父类的sleep方法，由于多个父类都有sleep方法，Python将使用父类列表的第一个父类的方法来继承
    c1.sleep()

    print(c1)