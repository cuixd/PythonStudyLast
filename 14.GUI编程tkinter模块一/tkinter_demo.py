import tkinter

# 开启一个窗口
win = tkinter.Tk()

# 为窗口指定标题名称
win.title("cuixd window")

print(type(win))
# 设置窗口大小长x高 + 左上角坐标位置 880+20，以电脑屏幕的左上角为(0,0)点
#win.geometry("600x400+200+20")


# 标签 label控件
label = tkinter.Label(win,
                      text="这是",
                      bg="pink",
                      fg="blue",
                      font="黑体, 20",
                      width=30,
                      #height=30,
                      #wraplength=50,
                      justify="right",
                      anchor="w")
label.pack()

def sayHello():
    print("Hello world")


# button按钮控件
# command指定点击时触发的事件，执行sayHello函数
# button1 = tkinter.Button(win,
#                         text="按钮1",
#                         width=10,
#                         height=10,
#                         command=sayHello)
# button1.pack()

# 指定执行匿名函数lamba
# command还可以指定 win.quit，点击触发窗口退出
button2 = tkinter.Button(win,
                        text="按钮2",
                        width=10,
                        height=10,
                        #command=lambda :print("我是button2")
                        command=win.quit)
button2.pack()

# Entry输入文本框控件
e = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=e)
e.set("请输入内容")

entry.pack()

content = e.get()

def getEntryValue():
    print(entry.get())

button3 = tkinter.Button(win,
                        text="按钮3",
                        width=10,
                        height=10,
                        #command=lambda :print("我是button2")
                        command=getEntryValue)
button3.pack()

# 滚动条控件
scroll = tkinter.Scrollbar()

# 文本框 text控件
text = tkinter.Text(win, width=30, height=10,bg="pink",fg="blue", font="黑体, 20")

# 设置滚动条的属性，在右边，长度布满窗口的右侧
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# 设置文本框属性，在左边，同样填满窗口纵向
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

# 设置滚动条与文本框纵向移动关联
scroll.config(command=text.yview)
# 设置文本框与滚动条关联
text.config(yscrollcommand=scroll.set)

str = '''
余告之曰：“其形也，翩若惊鸿，婉若游龙。荣曜秋菊，华茂春松。髣髴兮若轻云之蔽月，飘飖兮若流风之回雪。
远而望之，皎若太阳升朝霞；迫而察之，灼若芙蕖出渌波。秾纤得衷，修短合度。肩若削成，腰如约素。延颈秀项，
皓质呈露。芳泽无加，铅华弗御。云髻峨峨，修眉联娟。丹唇外朗，皓齿内鲜，明眸善睐，靥辅承权。瑰姿艳逸，
仪静体闲。柔情绰态，媚于语言。奇服旷世，骨像应图。披罗衣之璀粲兮，珥瑶碧之华琚。戴金翠之首饰，
缀明珠以耀躯。践远游之文履，曳雾绡之轻裾。微幽兰之芳蔼兮，步踟蹰于山隅。于是忽焉纵体，以遨以嬉。
左倚采旄，右荫桂旗。壤皓腕于神浒兮，采湍濑之玄芝。余情悦其淑美兮，心振荡而不怡。无良媒以接欢兮，
托微波而通辞。愿诚素之先达兮，解玉佩以要之。嗟佳人之信修，羌习礼而明诗。抗琼珶以和予兮，指潜渊而为期。
执眷眷之款实兮，惧斯灵之我欺。感交甫之弃言兮，怅犹豫而狐疑。收和颜而静志兮，申礼防以自持。
'''
# 设置文本框中的内容
text.insert(tkinter.INSERT, str)

win.mainloop()

