name = input('输入姓名：')
age = input('输入年龄：')
job = input('输入工作：')
hobbie = input('输入爱好：')

# 占位符为%，如果就是想要打%，那么使用%进行转义，而不是\
msg = '''
--------- info of %s ------
Name : %s
Age :  %d
Job :  %s
Hobbie : %s
---------------------------------
我就是想打印百分号%%
''' % (name, name, int(age), job, hobbie)

print(msg)
user = {'c': 1}

print(user)
