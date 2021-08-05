from wall_blogs.models import Category, Post
from django.contrib import admin



@admin.register(Post, Category)
class PostAdmin(admin.ModelAdmin):
    pass


