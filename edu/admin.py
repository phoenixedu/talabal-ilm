from django.contrib import admin
from .models import xEduInstitution,InstCourse,Book,InstitutionType,Semester,InstMediaUrls,userEdu,eduStorage

# Register your models here.
admin.site.register(xEduInstitution)
admin.site.register(InstCourse)
admin.site.register(InstitutionType)
admin.site.register(InstMediaUrls)
admin.site.register(Book)
admin.site.register(Semester)
admin.site.register(userEdu)
admin.site.register(eduStorage)