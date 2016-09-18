from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("article", "to_comment", "status", "owner", "content")

admin.site.register(Comment, CommentAdmin)
