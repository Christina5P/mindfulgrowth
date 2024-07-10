from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here for administrative interface

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status','created_on')
    search_fields = ['title', 'content']
    list_filter = ('categories',)
    summernote_fields = ('content',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin panel for comments"""
    list_display = ('post', 'name', 'body', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ['name', 'email', 'body']
