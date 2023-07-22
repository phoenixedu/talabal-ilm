from django import forms
from .models import eduClass,eduDepartment,eduLab,eduRole,eduSociety
from edu.models import InstCourse,Semester

class eduDepartmentForm(forms.ModelForm):
    class Meta:
        model = eduDepartment
        fields = ['name','location','picture']

class eduClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        edu = kwargs.pop('edu', None)
        super().__init__(*args, **kwargs)

        if edu:
            self.fields['department'].queryset = eduDepartment.objects.filter(edu=edu)
            self.fields['course'].queryset = InstCourse.objects.filter(edu=edu)
            self.fields['semister'].queryset = Semester.objects.filter(course__edu=edu)
    class Meta:
        model = eduClass
        fields = ['name','course','semister','department','picture','capacity','location']
        
class eduLabForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        edu = kwargs.pop('edu', None)
        super().__init__(*args, **kwargs)

        if edu:
            self.fields['department'].queryset = eduDepartment.objects.filter(edu=edu)
    class Meta:
        model = eduLab
        fields = ['name','location','department']
        
class eduRoleForm(forms.ModelForm):
    class Meta:
        model = eduRole
        fields = ['name','seats']


class eduSocietyForm(forms.ModelForm):
    class Meta:
        model = eduSociety
        fields = ['name','picture']