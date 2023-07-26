from django.contrib import admin
from .models import jobCvForm,studentAdmitForm,eduStudents,eduFaculty

# Register your models here.
admin.site.register(jobCvForm)
admin.site.register(studentAdmitForm)
admin.site.register(eduFaculty)
admin.site.register(eduStudents)
