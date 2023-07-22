from django import forms
from .models import ClassOfStudents,Electure,electureNotes
from edu_members.models import EduMember,eduFaculty
from edu_stracture.models import eduClass

class ClassOfStudentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        edu = kwargs.pop('edu', None)
        super().__init__(*args, **kwargs)

        if edu:
            self.fields['Eclass'].queryset = eduClass.objects.filter(edu=edu)
            self.fields['incharge'].queryset = eduFaculty.objects.filter(edu=edu)
    class Meta:
        model = ClassOfStudents
        fields = ['Eclass','name','incharge']

class EletureForm(forms.ModelForm):
    class Meta:
        model = Electure
        fields = ['teacher','title','video']
    def save(self, commit=True):
        if not self.cleaned_data['video']:
            self.instance.video = None
        return super().save(commit=commit)
    
class electureNotesForm(forms.ModelForm):
    class Meta:
        model = electureNotes
        fields = ['title','notes']