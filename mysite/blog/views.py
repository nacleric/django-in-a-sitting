from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse #take out HttpResponse later
from django.template import loader

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from .models import BlogPost, Comment

#NOTES: @login_required #for views that require person to log-in like creating commetns
#@login_required(redirect_field_name='my_redirect_field')

def index(request): #queries through all posts
    blogposts = BlogPost.objects.all()
    context = {'blogposts': blogposts}
    return render(request, 'blog/index.html', context)

def get_profile(request, user_id): #using the default user class now
    users = User.objects.get(pk=user_id) #queries the object
    username_obj = users.username #retrieves object attribute
    email_obj = users.email
    profile = "Username: " + username_obj + " Email: " + email_obj
    return HttpResponse(profile)

def get_blogpost(request, blogpost_id): #queries singular post
    blogpost = BlogPost.objects.get(pk=blogpost_id) 
    title_obj = blogpost.title
    author_obj = blogpost.author.username
    body_obj = blogpost.body 
    foo = "Title: " + title_obj + " author: " + author_obj + " body: " + body_obj 
    return HttpResponse(foo)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    '''
    if request.user.is_authenticated:
        pass
    else:
        pass
    '''










# Create your views here.
