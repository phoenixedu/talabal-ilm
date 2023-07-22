from django import forms
from .models import jobCvForm,studentAdmitForm

class JobAppliCvForm(forms.ModelForm):
    class Meta:
        model = jobCvForm
        fields = ['postalCode','address1','address2','religion','provence',
                'city','Districe','Tehsil','anyHonorsAwards','cv']

class StudenAddmissionPanddingForm(forms.ModelForm):
    class Meta:
        model = studentAdmitForm
        fields= ['nameOfGardiner','contactOfGardiner','postalCode','address1','address2','religion','provence',
                 'city','Districe','Tehsil','hafaza_Quran','educlass','lastResult','gradeLvl',
                 'anyHonorsAwards','cv']