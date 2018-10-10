import time
class Person(object):

    def __init__(self,name):
        self.name = name

    def fire(self,gun):

        if gun.getBullet() > 0:
            print("%s使用%s进行射击" % (self.name, gun.name))
            gun.shoot()
            print("%s当前还剩%d枚子弹" % (gun.name, gun.bullet))
        else:
            print("%s已经没子弹了，%s你不能再射击了" %(gun.name, self.name))


class Gun(object):

    def __init__(self,name,bullet):
        self.name = name
        self.bullet = bullet

    def shoot(self):
        print("%s射出了一枚子弹" % (self.name))
        self.bullet -= 1

    def getBullet(self):
        return self.bullet

gun1 = Gun("AWM狙击步枪",8)
p1 = Person("陈金宇")

while gun1.getBullet() > 0:
    time.sleep(2)
    p1.fire(gun1)

p1.fire(gun1)