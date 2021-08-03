from django.contrib import admin
from .models import Posting, Comment


class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'created_at', 'updated_at')
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')


class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('id', 'posting', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'content')


admin.site.register(Posting, PostingModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
