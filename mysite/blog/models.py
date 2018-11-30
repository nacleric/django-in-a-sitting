from django.db import models
from django.contrib.auth.models import User #AbstractUser

''' my original User model
class User(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100,default='placeholder-pw')
    def __str__(self):
        return self.username
'''
'''
class User(AbstractUser): custom user model
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100,default='placeholder-pw')
    def __str__(self):
        return self.username
'''
#remember to not allow users from liking or disliking multiple times
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=600)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Comment(models.Model):
    op = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=600)
    def __str__(self):
        return self.author.username

# Create your models here.
