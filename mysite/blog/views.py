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

'''probably doesnt work
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
'''
'''
def signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    if form.is_valid():
        user = User.objects.create_user(username,email,password)
    pass
'''
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user) #remember to make a template that lets u know person is logged in
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...    
'''
def logout(request):
    logout(request)
    pass
'''








# Create your views here.
