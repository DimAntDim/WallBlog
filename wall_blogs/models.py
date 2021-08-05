from django.db import models
from wall_profiles.models import Profile



class Category(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
        null=True,
        blank=False,
       
    )

class Post(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        null=True,
    )
    title = models.CharField(
        max_length=20,
        null=True,
        blank=False,
    )
    image = models.ImageField(
        upload_to = "posts/img/"
    )
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    text = models.TextField(
        null=True,
        blank=False,
    )
    creator = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
    )
    update = models.DateTimeField(
        auto_now=True,
    )
    user_owned = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

