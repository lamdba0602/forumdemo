from django.conf.urls import url

from .views import message_list
from .views import message_read

urlpatterns = [
    url(r'^list$', message_list),
    url(r'^read/(?P<message_id>\d+)', message_read),
]
