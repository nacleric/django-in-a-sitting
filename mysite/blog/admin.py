from django.contrib import admin
from django.contrib.auth.models import User
from .models import BlogPost, Comment

admin.site.register(BlogPost)
admin.site.register(Comment)

# Register your models here.
