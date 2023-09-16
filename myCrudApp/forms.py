from django import forms

from myCrudApp.models import University


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
    university_id = forms.IntegerField()
    FCs = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    year_of_admission = forms.DateField()
