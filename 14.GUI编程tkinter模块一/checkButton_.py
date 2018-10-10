import tkinter

win = tkinter.Tk()

win.title("tkinter window")
win.geometry("600x400+300+20")


def getMessage():
    message = ""
    if v1.get() == True:
        message += "王者荣耀\n"
    if v2.get() == True:
        message += "绝地求生\n"
    if v3.get() == True:
        message += "金钱美女\n"

    # 清除text的内容
    text.delete(0.0,tkinter.END)
    # 添加message到text
    text.insert(tkinter.INSERT, message)

# 定义描述复选框选中状态的变量
v1 = tkinter.BooleanVar()
# 定义复选框，指定名称，选中状态的变量，执行命令
ckb1 = tkinter.Checkbutton(win, text="王者荣耀", variable=v1, command=getMessage)

v2 = tkinter.BooleanVar()
ckb2 = tkinter.Checkbutton(win, text="绝地求生", variable=v2, command=getMessage)

v3 = tkinter.BooleanVar()
ckb3 = tkinter.Checkbutton(win, text="金钱美女", variable=v3, command=getMessage)

ckb1.pack()
ckb2.pack()
ckb3.pack()

text = tkinter.Text(win, width=300, height=50, bg="yellow")
text.pack()



win.mainloop()