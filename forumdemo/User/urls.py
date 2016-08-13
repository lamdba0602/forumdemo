from django.conf.urls import url

from .views import User_register

urlpatterns = [
    url(r'^register', User_register),
]
