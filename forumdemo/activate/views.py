from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Activate
import uuid


def activate_prepare(request):
    user = int(request.GET['id'])
    user_obj = User.objects.get(id=user)
    if user_obj.is_active is False:
        code = str(uuid.uuid4()).replace('-', "")
        activate = Activate(user=user_obj, code=code)
        activate.save()
        email = user_obj.email
        activate_link = "http://%s/activate/%s?id=%s" % (request.get_host(), code, user)
        activate_email = '点击<a href = "%s">这里</a>激活' % activate_link
        send_mail(subject='[Python 部落论坛]激活邮件',
                message='点击链接: %s' % activate_link,
                html_message=activate_email,
                from_email='743759846@qq.com',
                recipient_list=[email],
                fail_silently=False)
        return render(request, "activate_prepare.html")


def activate_deal(request, code):
    user = int(request.GET['id'])
    user_obj = User.objects.get(id=user)
    if user_obj.is_active is False:
        activate_obj = Activate.objects.get(user=user)
        if activate_obj.code == code:
            user_obj.is_active = True
            user_obj.save()
    return render(request, "activate_success.html")
