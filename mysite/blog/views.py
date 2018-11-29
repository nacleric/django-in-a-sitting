from django.shortcuts import render
from django.http import Http404, HttpResponse #take out HttpResponse later
from django.template import loader

#from django.contrib.auth.models import User #might remove this
from .models import User, BlogPost

def index(request): #queries through all posts
    blogposts = BlogPost.objects.all()
    context = {'blogposts': blogposts}
    return render(request, 'blog/index.html', context)

def get_profile(request, user_id): 
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

# def login(request):
#    new_user = User.objects.create_user('')





# Create your views here.
