from django.contrib import admin
from .models import Post
from category.models import Category

# Register your models here for administrative interface

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    filter_horizontal = ('categories',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')