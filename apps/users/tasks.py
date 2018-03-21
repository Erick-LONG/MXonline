from MXonline.celery1 import app
from random import Random
from utils.email_send import send_mail
from .models import EmailVerifyRecord
from MXonline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str

@app.task
def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://www.imooc.com/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "慕学在线网注册密码重置链接"
        email_body = "请点击下面的链接重置密码: http://www.imooc.com/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "慕学在线邮箱修改验证码"
        email_body = "你的邮箱验证码为: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

#4. 编辑views.py文件完成邮件发送异步调用：

    #coding:utf-8
    from django.shortcuts import render
    from django.http import HttpResponse

    from .tasks import send_register_email

    def index(request):
        send_register_email.delay()
        return HttpResponse(u"邮件发送成功， 请查收")

#5. 进入MxOnline目录运行：
 #   celery -A demo worker -l debug

  #  以此来启动celery的worker服务