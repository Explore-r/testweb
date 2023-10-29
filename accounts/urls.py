from django.urls import path
# from .import views
from accounts.views import *
# app_name ='accounts'

urlpatterns = [

    path('home/',home),
    path('products/',products),
    path('customer/',customer),
    path('login/',login),
    path('register/',register),
]