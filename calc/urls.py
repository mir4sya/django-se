from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('home',views.home, name = 'home'),
    path('highest',views.highest, name = 'highest'),
    path('lowest',views.lowest, name = 'lowest'),
    path('daily',views.daily, name = 'daily'),
    path('monthly',views.monthly, name = 'monthly'),
    path('weekly',views.weekly, name = 'weekly'),
    path('total',views.total, name = 'total'),
   
   
]

