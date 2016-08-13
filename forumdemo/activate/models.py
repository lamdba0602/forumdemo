from django.db import models
from django.contrib.auth.models import User


class Activate(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    code = models.CharField("激活码", max_length=100)
    deadline = models.DateTimeField("过期日期", auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "激活码"
        verbose_name_plural = "激活码"
