from django import forms
from .models import InstCourse, Semester, Book, xEduInstitution

class InstCourseForm(forms.ModelForm):
    class Meta:
        model = InstCourse
        fields = ['name','duration','descripition','totalfee','totalSimsters']
    
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name','duration','description','fee','books']


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        edu = kwargs.pop('edu', None)
        super().__init__(*args, **kwargs)
        if edu:
            self.fields['course'].queryset = InstCourse.objects.filter(edu=edu)
    class Meta:
        model = Book
        fields = ['name', 'author', 'publication', 'link', 'course']
         


class xEduInstitutionForm(forms.ModelForm):
    class Meta:
        model = xEduInstitution
        fields = ['name','typeOfInstitution','email','country','phone','address','picture']
                  
                
class updateEDU(forms.ModelForm):
    class Meta:
        model = xEduInstitution
        fields = ['name','email','country','phone','address','picture']

class updateCourse(forms.ModelForm):
    class Meta:
        model = InstCourse
        fields = ['name','duration','descripition','totalfee','totalSimsters']

class updateSemester(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name','duration','description','fee','books']
    
                  
