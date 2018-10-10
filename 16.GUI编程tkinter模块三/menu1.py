import tkinter

win = tkinter.Tk()
win.title("鼠标右键菜单演示")

win.geometry("600x400+300+20")

# 定义一个菜单条，这里其实就是鼠标右键后显示的第一级菜单
menubar = tkinter.Menu(win)

# 定义菜单，存放在第一级菜单中
menu = tkinter.Menu(menubar, tearoff=False)

for item in ["王者荣耀", "绝地求生", "传奇私服", "尤里复仇", "魔兽争霸"]:
    # 为菜单添加菜单项，label指定显示名称，command指定点击事件
    menu.add_command(label=item)

menubar.add_cascade(label="游戏", menu=menu)
# 右键显示菜单事件
def showMenu(event):
    menubar.post(event.x_root, event.y_root)

#窗体绑定鼠标右键单击事件，mac上是2，windows下可能是3
win.bind("<Button-2>", showMenu)


'''
多级子菜单
'''
# 定义另外一个菜单
menu2 = tkinter.Menu(menubar, tearoff=False)

# 使用for循环动态添加子菜单
for item in ["Java", "Python", "C++"]:

    # 使用locals()方法动态创建变量名"menu"+列表元素值，并创建菜单
    locals()["menu"+item] = tkinter.Menu(menu2)
    # 为每个菜单添加菜单项
    locals()["menu" + item].add_command(label="我不会")
    locals()["menu" + item].add_command(label="这个我会")

    # 将动态创建的菜单关联到主菜单
    menu2.add_cascade(label=item, menu=locals()["menu"+item])

# 主菜单关联到第一级菜单
menubar.add_cascade(label="语言", menu=menu2)

win.mainloop()