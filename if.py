# -*- encoding:utf8 -*-


while True:
    age = int(input('输入你的猜数：'))
    if age < 18:
        print('太小了')
    elif age > 18:
        print('太大了')
    else:
        print('你猜对了:', age)
        break