import tkinter

win = tkinter.Tk()

win.title("框架frame示例窗口")
win.geometry("600x400+300+20")

frm = tkinter.Frame(win, bg="pink")
frm.pack()

frm_1 = tkinter.Frame(frm)

label1 = tkinter.Label(frm_1, text="左上", bg="blue")
label2 = tkinter.Label(frm_1, text="左下", bg="red")
label1.pack(side=tkinter.TOP)
label2.pack(side=tkinter.TOP)

frm_1.pack(side=tkinter.LEFT)

frm_2 = tkinter.Frame(frm)
label3 = tkinter.Label(frm_2, text="右上", bg="orange")
label4 = tkinter.Label(frm_2, text="右下", bg="yellow")
label3.pack(side=tkinter.TOP)
label4.pack(side=tkinter.TOP)

frm_2.pack(side=tkinter.RIGHT)

win.mainloop()