import tkinter

win = tkinter.Tk()
win.title("menu window")
win.geometry("600x400+300+0")

# 定义一个菜单条
menubar = tkinter.Menu(win)
# 将菜单条配置到窗体
win.config(menu=menubar)

# 定义一个菜单
menu1 = tkinter.Menu(menubar, tearoff=True)

# 定义菜单项被点击时的事件函数
def getItem():
    print("哈哈，我爱玩")


for item in ["王者荣耀", "绝地求生", "传奇私服", "尤里复仇", "魔兽争霸"]:
    # 为菜单添加菜单项，label指定显示名称，command指定点击事件
    menu1.add_command(label=item, command=getItem)
    #菜单项之间添加分割线
    menu1.add_separator()
# 将菜单放入菜单条，label指定菜单的名称
menubar.add_cascade(label="游戏", menu=menu1)

win.mainloop()