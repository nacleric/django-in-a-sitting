from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse #take out HttpResponse later
from django.template import loader
from django.contrib.auth import login, logout, authenticate