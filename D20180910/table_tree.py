import tkinter
from tkinter import ttk


win = tkinter.Tk()

win.title("框架frame示例窗口")
win.geometry("600x400+300+20")

# 创建一个表格或树形结构
table = ttk.Treeview(win)
table.pack()

# 定义表格的列
table["columns"]=("name","age","height","weight")

# 设置每个列的宽度
table.column("name", width=100)
table.column("age", width=100)
table.column("height", width=100)
table.column("weight", width=100)

# 设置每个列的头，并指定显示名称
table.heading("name", text="姓名")
table.heading("age", text="年龄")
table.heading("height", text="身高")
table.heading("weight", text="体重")

# 插入数据，第一个字段空字符串表示该数据所属的上级为空，即顶级，第二个字段表示数据行标识，从0开始
# values是真正插入的值，元组
table.insert("", 0, text="line1", values=("崔晓东", 33, 176, 75))
table.insert("", 1, text="line2", values=("程咬金", 13, 176, 75))


# 定义一个树状结构，跟前面表状的一样
tree = ttk.Treeview(win)
tree.pack()

# 插入根节点
treeroot1 = tree.insert("", 0, "中国", text="中国", values="CHN")
treeroot2 = tree.insert("", 1, "美国", text="美国", values="USA")

# 在中国这个根节点下插入一级节点
leaf1_1 = tree.insert(treeroot1, 0, "浙江", text="浙江", values="ZJ")
leaf1_2 = tree.insert(treeroot1, 1, "江苏", text="江苏", values="JS")

# 在两个省份一级节点下各自插入两个二级城市节点
leaf2_11 = tree.insert(leaf1_1, 0, "杭州", text="杭州", values="hz")
leaf2_12 = tree.insert(leaf1_1, 1, "宁波", text="宁波", values="nb")

leaf2_21 = tree.insert(leaf1_2, 0, "南京", text="南京", values="nj")
leaf2_22 = tree.insert(leaf1_2, 1, "盐城", text="盐城", values="yc")

win.mainloop()