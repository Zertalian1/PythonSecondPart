from django.contrib import admin
from django.urls import path

import myCrudApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', myCrudApp.views.index, name="home"),
    path('api/create-university', myCrudApp.views.create_university, name="home"),
    path('api/edit-university', myCrudApp.views.edit_university, name="home")
]
