from django.urls import path
#might be deprecated from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/profile/', views.get_profile, name='profile'),
    path('<int:blogpost_id>/blogpost/', views.get_blogpost, name='blogpost'),
    #path('/signup', views.signup, name='signup'), #probably busted
    #path('/login', auth_views.login, name='login'), #not dun
    #path('/logout', auth_views.logout, name='logout'), #not dun


]