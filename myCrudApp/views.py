from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django import forms

from myCrudApp.forms import UniversityForm
from myCrudApp.models import University


def index(request):
    return TemplateResponse(request, "index.html")


def create_university(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        short_name = request.POST.get("short_name")
        date_of_creation = request.POST.get("date_of_creation")
        university = University.objects.create(
            full_name=full_name,
            short_name=short_name,
            date_of_creation=date_of_creation
        )
        return HttpResponseRedirect(f"/api/university/{university.id}")
    if request.method == "GET":
        data = {"form": UniversityForm()}
        return TemplateResponse(request, "createUniversity.html", data)


def edit_university(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        short_name = request.POST.get("short_name")
        date_of_creation = request.POST.get("date_of_creation")
        university = University.objects.filter(id=1).update(
            full_name=full_name,
            short_name=short_name,
            date_of_creation=date_of_creation
        )
        return HttpResponseRedirect(f"/api/university/{university.id}")
    if request.method == "GET":
        data = {"form": UniversityForm()}
        return TemplateResponse(request, "createUniversity.html", data)


def university(request, id):
    if request.method == "GET":
        data = {"university": University.objects.get(id=id)}
        return TemplateResponse(request, "University.html", data)
