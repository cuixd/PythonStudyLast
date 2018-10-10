import calendar

# 日历模块

# 获取指定某个月的日历
c1 = calendar.month(2018, 8)
print(c1)

# 产生一个整年的日历
c2 = calendar.calendar(2018)
print(c2)

# 判断是否为闰年
c3 = calendar.isleap(2018)
print(c3)

# 返回某个月份的第一天所属的weekenday（星期N-1） 及当月总天数
c4 = calendar.monthrange(2018,8)
print(c4)

# 获取某个月份的日历列表，每周七天为一个元素
c5 = calendar.monthcalendar(2018,8)
print(c5)