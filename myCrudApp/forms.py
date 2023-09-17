from django import forms

from myCrudApp.models import University, Student


class DateInput(forms.DateInput):
    input_type = 'date'


class UniversityForm(forms.ModelForm):

    class Meta:
        model = University
        fields = '__all__'
        widgets = {
            'date_of_creation': DateInput()
        }


class StudentForm(forms.Form):
    model = Student
    fields = '__all__'
