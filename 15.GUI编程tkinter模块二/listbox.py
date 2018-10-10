import tkinter

'''
列表框

'''


win = tkinter.Tk()

win.title("list box window")
win.geometry("600x400+300+20")

# 定义一个listbox 选择模式selectmode BROWSE 鼠标按下拖动时，跟踪鼠标位置选中对应条目
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb.pack()
for item in ["王者荣耀", "绝地求生", "传奇私服", "尤里复仇", "魔兽争霸"]:

    # 在列表的尾部顺序添加
    lb.insert(tkinter.END, item)

# 列表顶部添加元素
lb.insert(tkinter.ACTIVE, "红色警戒")

# 删除元素范围，开始下标，结束下标
# lb.delete(1,3)

# 删除单个元素
lb.delete(2)

# 选中元素范围
lb.select_set(2, 4)

# 取消选中范围
#lb.select_clear(2, 4)

# 选中一个元素
#lb.select_set(2)

# 取消选中单个元素
#lb.select_clear(2)

# 列表中元素的个数
print(lb.size())

# 获取一段范围的元素值，返回元组
print(lb.get(2, 4))
# 获取单个元素值
print(lb.get(2))

# 范围当前选中元素的下标，如果选中一段范围，则是范围内的各元素下标，如果是单个选中，则是该元素下标后加逗号,
print(lb.curselection())

# 判断某个下标元素是否被选中，返回True或False
print(lb.select_includes(2))
print(lb.select_includes(1))

win.mainloop()