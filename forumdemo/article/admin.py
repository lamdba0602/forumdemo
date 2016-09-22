from django.contrib import admin

from .models import Article
from comment.models import Comment


class CommentInline(admin.TabularInline):
    model = Comment
    can_delete = False


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "block", "status", "owner")
    actions = ['make_picked']
    inlines = [CommentInline]

    def make_picked(modeladmin, request, queryset):
        for a in queryset:
            a.status = 10
            a.save()
    make_picked.short_description = "设置精华"

    fieldsets = (
            ('基本',
            {
                "fields": ("title", "content")
            }    
            ),
            ("高级",
            {
                "classes": ('collapse',),
                "fields": ("status",)
            }
            )
            )
    readonly_fields = ("owner", "content", "status")

admin.site.register(Article, ArticleAdmin)
