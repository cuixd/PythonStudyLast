import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("下拉框列表")
win.geometry("600x400+300+20")

comv = tkinter.StringVar()
comb = ttk.Combobox(win, textvariable=comv)

comb.pack()

comb["value"] = ("Java", "Python", "Oracle")
comb.current(0)

def getValue(event):

    #获取选中项的值，可以使用绑定变量获取，也可以通过控件变量直接获取
    print(comv.get())
    print(comb.get())

# 绑定一个获取当前选定值的事件
comb.bind("<<ComboboxSelected>>", getValue)


win.mainloop()