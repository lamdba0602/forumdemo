from django.contrib import admin

from .models import Activate

class ActivateAdmin(admin.ModelAdmin):
        list_display = ("user", "code", "deadline")

admin.site.register(Activate, ActivateAdmin)
