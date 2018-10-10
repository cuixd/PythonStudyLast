import tkinter

win = tkinter.Tk()
win.title("listbox single window")
win.geometry("600x400+300+20")

# 定义listbox中的绑定变量，类型string
lbv = tkinter.StringVar()

# selectmode=tkinter.SINGLE 鼠标按下拖动时，选中条目不随着鼠标位置的改变而改变
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)   # type:tkinter.Listbox
lb.pack()

for item in ["关羽", "张飞", "马超", "赵云", "黄忠", "夏侯惇", "典韦"]:
    lb.insert(tkinter.END, item)

# 通过绑定变量获取列表内容
print(lbv.get())

# 通过控件对象get全部值
print(lb.get(0,tkinter.END))
# 通过绑定变量设置全部值 覆盖
lbv.set(("王者荣耀", "绝地求生", "传奇私服", "尤里复仇", "魔兽争霸"))

print(lbv.get())

# 定义事件函数
def getItemText(event):
    print(lb.get(lb.curselection()))

# 控件绑定双击事件 <Double-Button-1> 表示鼠标左键双击事件，固定写法， 1表示左键
lb.bind("<Double-Button-1>", getItemText)

win.mainloop()