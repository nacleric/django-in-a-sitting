from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def get_username(request, user_id):
	user_object = User.objects.get(pk=user_id) #queries the object
	query = user_object.username #retrieves object attribute
	return HttpResponse("Your looking at user: %s." % query)

def get_email(request, user_id):
	user_object = User.objects.get(pk=user_id)
	query = user_object.email
	return HttpResponse("Looking at email: %s." % query)

# Create your views here.
