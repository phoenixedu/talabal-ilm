from django.db import models
from django.contrib.auth.models import User
from edu.models import xEduInstitution,InstCourse,Semester
import random
import os
from django.utils import timezone

def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    filename = f'{instance.castStr()}-{random_numbers}.{ext}'
    return os.path.join('images/stracture', filename)

class eduDepartment(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    picture = models.ImageField(upload_to=upload_path,blank=True)
    dateOfcreation = models.DateField(default=timezone.now,editable=False)

    def castStr(self):
        return str(f"dpt-{self.name}")
         
    def __str__(self):
        return self.name

class eduClass(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE)
    course = models.ForeignKey(InstCourse, on_delete=models.CASCADE)
    semister = models.ForeignKey(Semester, on_delete=models.CASCADE)
    department = models.ForeignKey(eduDepartment,blank=True,null=True ,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=150)
    picture = models.ImageField(upload_to=upload_path,blank=True)
    dateOfcreation = models.DateField(default=timezone.now,editable=False)

    def castStr(self):
        strd = str(f"cls-{self.name}")
        return strd
    
    def __str__(self):
        return self.name
    
class eduLab(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    department = models.ForeignKey(eduDepartment,null=True,blank=True, on_delete=models.CASCADE)
    dateOfcreation = models.DateField(default=timezone.now,editable=False)

    def __str__(self):
        return self.name
    
class eduSociety(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    picture = models.ImageField(upload_to=upload_path,blank=True)
    dateOfcreation = models.DateField(default=timezone.now,editable=False)

    def castStr(self):
        strd = str(f"sty-{self.name}")
        return strd

    def __str__(self):
        return self.name

class eduRole(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    seats = models.IntegerField()
    dateOfcreation = models.DateField(default=timezone.now,editable=False)

    def __str__(self):
        return self.name
    


