

class Mather:

    def __init__(self,facevalue, mname):

        self.faceValue = facevalue
        self.__mname = mname

    def cook(self):

        print("做饭")

    def wash(self):

        print("洗衣")

    def sleep(self):
        print("安静的睡")

    def getMname(self):

        return self.__mname