from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
from django.contrib import messages
import uuid
import random
import os 
# Create your models here.

def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    filename = f'{instance.name}-{instance.uuid}-{random_numbers}.{ext}'
    return os.path.join('images/eduOrg', filename)

class InstitutionType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class xEduInstitution(models.Model):
    OwnerOfX = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    typeOfInstitution = models.ForeignKey(InstitutionType, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    email = models.EmailField()
    country = CountryField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=upload_path, blank=True)
    registration_date = models.DateField(default=timezone.now , editable=False)
    pk_key = models.CharField( unique=True, max_length=255)
    active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        self.nameKy = self.name.replace(" ", "_")
        self.pk_key = self.nameKy + str(self.uuid)[:5]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class InstMediaUrls(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200) 

    def __str__(self):
        return f'{self.name}'
    
class InstCourse(models.Model):
    id = models.AutoField(primary_key=True)
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False)
    duration = models.CharField(max_length=75,null=True,blank=True)
    descripition = models.TextField()
    totalfee = models.CharField(max_length=75,null=True,blank=True)
    totalSimsters = models.IntegerField(null=True,blank=True)
    smFull = models.BooleanField(default=False)

    '''def save(self, *args, **kwargs):
        if self.totalSimsters is not None:
            existing_semesters = Semester.objects.filter(course_id=self.id).count()
            if existing_semesters >= self.totalSimsters:
                self.smFull = True
        super().save(*args, **kwargs)'''

    def __str__(self):
        return f"{self.name}"  

class Book(models.Model):
    course = models.ManyToManyField(InstCourse,blank=True)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150,null=True,blank=True)
    publication = models.CharField(max_length=150,null=True,blank=True)
    link = models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Semester(models.Model):
    course = models.ForeignKey(InstCourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book, blank=True)
    duration = models.CharField(max_length=75)
    description = models.TextField()
    fee = models.CharField(max_length=75)

    def save(self, *args, **kwargs):
        if self.course.totalSimsters is not None:
            existing_semesters = Semester.objects.filter(course=self.course)
            if self.pk:
                existing_semesters = existing_semesters.exclude(pk=self.pk)
            existing_semesters_count = existing_semesters.count()
            if existing_semesters_count >= self.course.totalSimsters:
                raise ValueError("Cannot add more semesters than the specified total Simsters of respective course. ")
        super().save(*args, **kwargs)

    def __str__(self):
        return str(f"{self.name} | {self.course}")
    

