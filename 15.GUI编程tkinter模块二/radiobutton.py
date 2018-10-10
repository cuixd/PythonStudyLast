import tkinter

'''
单选框
'''


win = tkinter.Tk()

win.title("tkinter window")
win.geometry("600x400+300+20")

# 定义获取点选框值的方法，通过绑定的变量来获取
def getValue():
    print(var.get())

# 定义绑定同组单选框的变量，变量的类型要与单选框value值的类型一致，这里使用的是整形，推荐使用整形
var = tkinter.IntVar()

# 定义单选框， 显示文本text， 实际值value, 绑定变量, 点击事件
rb1 = tkinter.Radiobutton(win, text="one", value=1, variable=var, command=getValue)
rb1.pack()

rb2 = tkinter.Radiobutton(win, text="two", value=2, variable=var, command=getValue)
rb2.pack()

rb3 = tkinter.Radiobutton(win, text="three", value=3, variable=var, command=getValue)
rb3.pack()










win.mainloop()