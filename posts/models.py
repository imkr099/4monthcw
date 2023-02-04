from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
