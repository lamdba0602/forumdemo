from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("article", "status", "owner", "content")

admin.site.register(Comment, CommentAdmin)
