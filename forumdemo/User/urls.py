from django.conf.urls import url

from .views import User_register
from .views import User_login

urlpatterns = [
    url(r'^register', User_register),
    url(r'^login', User_login),
]
