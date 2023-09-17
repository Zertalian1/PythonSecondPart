from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.template.response import TemplateResponse

from myCrudApp.forms import UniversityForm, StudentForm
from myCrudApp.models import University, Student


def index(request):
    return TemplateResponse(request, "index.html")


def create_university(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        short_name = request.POST.get("short_name")
        date_of_creation = request.POST.get("date_of_creation")
        University.objects.create(
            full_name=full_name,
            short_name=short_name,
            date_of_creation=date_of_creation
        )
        return HttpResponseRedirect(f"/api/university")
    if request.method == "GET":
        data = {"form": UniversityForm()}
        return TemplateResponse(request, "createUniversity.html", data)


def edit_university_by_id(request, id):
    if request.method == "GET":
        university = University.objects.get(id=id)
        data = {"university": university}
        return TemplateResponse(request, "createUniversity.html", data)
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        short_name = request.POST.get("short_name")
        date_of_creation = request.POST.get("date_of_creation")
        University.objects.filter(id=id).update(
            full_name=full_name,
            short_name=short_name,
            date_of_creation=date_of_creation
        )
        return HttpResponseRedirect(f"/api/university")


def delete_university_by_id(request, id):
    if request.method == "GET":
        try:
            product = University.objects.get(id=id)
            product.delete()
            return HttpResponseRedirect("/api/university")
        except University.DoesNotExist:
            return HttpResponseNotFound("Университета с таким id не существует")


def get_all_university(request):
    if request.method == "GET":
        university_list = University.objects.all()
        data = {"universities": university_list}
        return TemplateResponse(request, "allUniversity.html", data)


def create_student(request):
    if request.method == "POST":
        student = Student()
        student.FCs = request.POST.get("FCs")
        student.date_of_birth = request.POST.get("date_of_birth")
        student.year_of_admission = request.POST.get("year_of_admission")
        student.university_id = request.POST.get("university")
        student.save()
        return HttpResponseRedirect(f"/api/student")
    if request.method == "GET":
        available_university_list = University.objects.all()
        data = {
            "student": StudentForm(),
            "available_university_list": available_university_list
        }
        return TemplateResponse(request, "createStudent.html", data)


def edit_student_by_id(request, id):
    if request.method == "GET":
        student = Student.objects.get(id=id)
        available_university_list = University.objects.all()
        data = {
            "student": student,
            "available_university_list": available_university_list
        }
        return TemplateResponse(request, "createStudent.html", data)
    if request.method == "POST":
        student = Student()
        student.FCs = request.POST.get("FCs")
        student.date_of_birth = request.POST.get("date_of_birth")
        student.year_of_admission = request.POST.get("year_of_admission")
        student.university_id = request.POST.get("university")
        University.objects.filter(id=id).update(student=student)
        return HttpResponseRedirect(f"/api/student")


def delete_student_by_id(request, id):
    if request.method == "GET":
        try:
            product = Student.objects.get(id=id)
            product.delete()
            return HttpResponseRedirect("/api/student")
        except University.DoesNotExist:
            return HttpResponseNotFound("Студента с таким id не существует")


def get_all_student(request):
    if request.method == "GET":
        student_list = Student.objects.all()
        data = {"students": student_list}
        return TemplateResponse(request, "allStudent.html", data)
