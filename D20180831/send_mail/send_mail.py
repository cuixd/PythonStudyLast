
import smtplib # 邮箱smtp服务包

from email.mime.text import MIMEText   #邮件文本处理模块

# 指定smtp服务器地址
SMTPServer = "smtp.163.com"

# 发件人
sender = "cxdwrmq@163.com"

# 密码，这个密码是在邮箱设置的客户端授权码，并不是邮箱的web登录密码，不过在mac的邮件app里可以登录
password = "cuixd1985"

# 邮件body内容
message = "我是你自己"

# 将邮件文本封装为api对象
msg = MIMEText(message)

print(type(msg))

# 邮件标题
msg["Subject"] = "来自帅哥的问候"

# 邮件发送者
msg["From"] = sender

# 创建smtp服务
mailServer = smtplib.SMTP(SMTPServer, 25)

# 登录服务器
mailServer.login(sender,password)

# 构造接收者邮箱列表
receiver = []
# receiver.append("zhigang.huang@xinguang.com")
# receiver.append("wanl@xinguangnet.com")
# receiver.append("bo.zhang@xinguang.com")
# receiver.append("panxia.li@xinguang.com")
# receiver.append("liyuan@xinguangnet.com")
receiver.append("cuixd@xinguangnet.com")

print(receiver)

# 发送邮件
mailServer.sendmail(sender,receiver, msg.as_string())

# 退出
mailServer.quit()
