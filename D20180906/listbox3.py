import tkinter

win = tkinter.Tk()
win.title("list box use extended mode")


# 定义listbox控件，使用extented模式，支持按shift进行连选，和按control进行多选
# 还有另一种mode叫MUTIPLE支持鼠标直接进行多选
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED)

for item in ["关羽", "张飞", "马超", "赵云", "黄忠", "夏侯惇", "典韦",
                                                  "王者荣耀", "绝地求生", "传奇私服", "尤里复仇", "魔兽争霸"]:
    lb.insert(tkinter.END, item)

# 显示控件，指定控件在窗口中的位置为左边，填满窗体横纵
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

# 定义滚动条
scroll = tkinter.Scrollbar(win)
# 显示滚动条，设置其在窗体的右边，填满窗体纵向
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# 配置滚动条与listbox控件的纵向移动相关联
#scroll.configure(command=lb.yview)

# 上面的配置其实就是指定command属性，也可以如下方式来设置
scroll["command"] = lb.yview
# 设置listbox控件与滚动条关联
lb.configure(yscrollcommand=scroll.set)

win.mainloop()