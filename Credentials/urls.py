from django.contrib.auth import views as auth_views
from . import views
from Credentials import views as user_views
from django.urls import path

app_name='Credentials'

urlpatterns = [
    path('register', user_views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),

]
