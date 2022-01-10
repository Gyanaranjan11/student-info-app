
from django import forms

from StudentinfoApp.models import StudentInfo, StudentAcademic


class StudentInfoFrom(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'


class StudentAcademicFrom(forms.ModelForm):
    class Meta:
        model = StudentAcademic
        fields = '__all__'
