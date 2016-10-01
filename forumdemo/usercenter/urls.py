from django.conf.urls import url

from .views import portrait_upload

urlpatterns = [
    url(r'^portrait_upload$', portrait_upload)
]
