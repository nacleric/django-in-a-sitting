from django.urls import path, include
#might be deprecated from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/profile/', views.get_profile, name='profile'),
    path('<int:blogpost_id>/blogpost/', views.get_blogpost, name='blogpost'),
    path('accounts/', include('django.contrib.auth.urls')),
    #provides accounts/... login,logout,passwordchange, paswordreset etc
]