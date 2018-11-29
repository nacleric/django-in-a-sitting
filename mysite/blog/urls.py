from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('/login', views.login, name='login')
    path('<int:user_id>/profile/', views.get_profile, name='profile'),
    path('<int:blogpost_id>/blogpost/', views.get_blogpost, name='blogpost'),


]