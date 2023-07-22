from django import forms
from .models import AdmissionFrom, jobRecruitry
from edu_stracture.models import eduRole
from edu.models import InstCourse


class AdmissionFromForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        edu = kwargs.pop('edu', None)
        super().__init__(*args, **kwargs)
        
        if edu:
            self.fields['course'].queryset = InstCourse.objects.filter(edu=edu)
    class Meta:
        model = AdmissionFrom
        fields = ['name','course','requirements','seats','sectionStart','sectionEnd','lastDate','bachno','ad']
    
    
class jobRecruitryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        edu = kwargs.pop('edu', None)
        super().__init__(*args, **kwargs)
        
        if edu:
            self.fields['forPost'].queryset = eduRole.objects.filter(edu=edu)
    class Meta:
        model = jobRecruitry
        fields = ['name','forPost','seats','joining','lastDate','requirements','ad']
        