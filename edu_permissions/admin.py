from django.contrib import admin
from .models import HeadOfTheDepartment,GroupOfAdmins,GroupOfSubHeadOfInstetude,GroupOfStudents,GroupOfTeachers,InchargeOfClass,HeadOfInstetude
# Register your models here.
admin.site.register(HeadOfTheDepartment)
admin.site.register(GroupOfSubHeadOfInstetude)
admin.site.register(GroupOfStudents)
admin.site.register(GroupOfTeachers)
admin.site.register(InchargeOfClass)
admin.site.register(GroupOfAdmins)
admin.site.register(HeadOfInstetude)