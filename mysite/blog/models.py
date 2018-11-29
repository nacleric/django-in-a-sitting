from django.db import models
from django.contrib.auth.models import AbstractUser

'''
class User(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100,default='placeholder-pw')
    def __str__(self):
        return self.username
'''
'''
class User(AbstractUser):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100,default='placeholder-pw')
    def __str__(self):
        return self.username
'''

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=600)
    def __str__(self):
        return self.title

# Create your models here.
