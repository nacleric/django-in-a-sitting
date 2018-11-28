from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/username/', views.get_username, name='username'),
    path('<int:user_id>/email/', views.get_email, name='email')
]