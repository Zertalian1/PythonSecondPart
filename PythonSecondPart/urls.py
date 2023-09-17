from django.contrib import admin
from django.urls import path

import myCrudApp.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api', myCrudApp.views.index, name="home"),

    path('api/university/create', myCrudApp.views.create_university, name="home"),
    path('api/university/edit/<int:id>', myCrudApp.views.edit_university_by_id, name="home"),
    path('api/university/delete/<int:id>', myCrudApp.views.delete_university_by_id, name="home"),
    path('api/university', myCrudApp.views.get_all_university, name="home"),

    path('api/student/create', myCrudApp.views.create_student, name="home"),
    path('api/student/edit/<int:id>', myCrudApp.views.edit_student_by_id, name="home"),
    path('api/student/delete/<int:id>', myCrudApp.views.delete_student_by_id, name="home"),
    path('api/student', myCrudApp.views.get_all_student, name="home")
]
