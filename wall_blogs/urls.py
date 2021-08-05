from wall_blogs.views import create_post
from django.urls import path

urlpatterns = [
    path('create/', create_post, name="create post"),
]
