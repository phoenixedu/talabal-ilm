from django.contrib import admin
from .models import ClassOfStudents,eClassVideos,Electure,Attendance
# Register your models here.

admin.site.register(ClassOfStudents)
admin.site.register(eClassVideos)
admin.site.register(Electure)
admin.site.register(Attendance)
