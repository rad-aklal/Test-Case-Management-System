from django.urls import path
from . views import login,home,register

urlpatterns =[
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
]