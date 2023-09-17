from django.contrib import admin

from myCrudApp.models import University, Student

class UniversityAdmin(admin.ModelAdmin):
    #Данная переменная указывает на поля, которые будут выводится в списке продуктов
    list_display = ('id', 'full name', 'short name', 'date of creation')

admin.site.register(University)
admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'FCs', 'date of birth', 'year of admission', 'university id')
