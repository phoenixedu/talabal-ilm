from django.contrib import admin
from .models import eduClass,eduDepartment,eduLab,eduRole,eduSociety
# Register your models here.
admin.site.register(eduClass)
admin.site.register(eduDepartment)
admin.site.register(eduLab)
admin.site.register(eduSociety)
admin.site.register(eduRole)
