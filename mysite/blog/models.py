from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=600)
    def __str__(self):
        bp = self.author + ':' + self.title
        return bp

# Create your models here.
