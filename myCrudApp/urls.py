from django.urls import path
from myCrudApp import views

urlpatterns = [
    #Вызовет views.index при открытии главной страницы сайта
    path('', "Test", name="home")
]