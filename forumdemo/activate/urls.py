from django.conf.urls import url

from .views import activate_prepare
from .views import activate_deal

urlpatterns = [
    url(r'^$', activate_prepare),
    url(r'^(?P<code>\w+)$', activate_deal),
]
