import tkinter

'''
滑动设置条 scale
'''

win = tkinter.Tk()
win.title("scale window")

win.geometry("600x400+300+20")


# 定义一个滑动条，设置开始和结束的值范围，orient表示滑动条的方向 HORIZONTAL水平方向，VERTICAL竖直方向
# tickinterval显示刻度间隔， length滑动条的长度
scale = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=20, length=200)
scale.pack()

# 获取滑动条的当前值
print(scale.get())

# 设置值
scale.set(34)


def getValue():
    print(scale.get())

# 定义一个按钮，点击事件来获取滑动条的当前值
button = tkinter.Button(win, text="按钮", command=getValue)


button.pack()

# 主窗体运行
win.mainloop()