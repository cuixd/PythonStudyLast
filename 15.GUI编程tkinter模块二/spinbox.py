import tkinter

'''
数值范围增减框
'''

win = tkinter.Tk()
win.title("spinbox window")

win.geometry("600x400+300+20")

def getValue():
    print(sbv.get())

sbv = tkinter.StringVar()


sb = tkinter.Spinbox(win, from_=0, to=100, increment=10, textvariable=sbv,
                     command=getValue)
sb.pack()

print(sbv.get())


win.mainloop()

