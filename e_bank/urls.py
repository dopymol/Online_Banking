from .import views
from django.urls import path
app_name='e_bank'

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('newpage',views.newpage,name='newpage'),
    path('formp',views.formp,name='formp'),
    path('thank',views.thank,name='thank'),


]