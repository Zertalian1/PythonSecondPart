from django.urls import path
from myCrudApp import views

urlpatterns = [
    #Вызовет views.index при открытии главной страницы сайта
    path('', views.index, name="home"),
    #Вызовет views.about при /about
    path('about', views.about, name="home"),
]