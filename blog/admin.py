from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Add fields which will use summernote editor in admin page
    """

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on',)
    list_display = ('title', 'slug', 'location', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for display in admin page
    """

    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'body']