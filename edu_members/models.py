from django.db import models
from django.contrib.auth.models import User,Group
from edu.models import xEduInstitution,InstCourse
from edu_stracture.models import eduRole
from edu_recruiter.models import AdmissionFrom,jobRecruitry
from django.utils import timezone
import uuid
import os 
import random

# Create your models here.

PENDING = 'Pending'
APPROVED = 'Approved'
REJECTED = 'Rejected'

STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
)

def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(10))
    filename = f'{instance.pathnm()}-{random_numbers}.{ext}'
    return os.path.join('pdf/educv', filename)


class studentAdmitForm(models.Model):
    userS = models.OneToOneField(User, on_delete=models.CASCADE)
    nameOfGardiner = models.CharField(blank=True, max_length=70)
    contactOfGardiner = models.CharField(blank=True, max_length=70)
    postalCode = models.CharField(blank=True, max_length=70)
    address1 = models.TextField(blank=True)
    address2 = models.TextField(blank=True)
    religion = models.CharField(max_length=120,blank=True)
    demicile = models.CharField(max_length=100,blank=True)
    provence = models.CharField(max_length=120,blank=True)
    city = models.CharField(max_length=120,blank=True)
    Districe = models.CharField(max_length=120,blank=True)
    Tehsil = models.CharField(max_length=120,blank=True)
    hafaza_Quran = models.BooleanField(default=False)
    educlass = models.CharField(max_length=70)
    admForm = models.ForeignKey(AdmissionFrom, on_delete=models.CASCADE)
    lastResult = models.CharField(max_length=300)
    gradeLvl = models.CharField(max_length=70)
    anyHonorsAwards = models.TextField(blank=True)
    course = models.ManyToManyField(InstCourse,blank=True)
    dateOfapplyed = models.DateTimeField(default=timezone.now,editable=False)
    student = models.BooleanField(default=True)
    cv = models.FileField(upload_to=upload_path,blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default=PENDING, max_length=20)

    def pathnm(self):
        return str(f"result_{self.userS}")

    def __str__(self):
        return str(self.userS)

class jobCvForm(models.Model):
    userS = models.OneToOneField(User, on_delete=models.CASCADE)
    admForm = models.ForeignKey(jobRecruitry, on_delete=models.CASCADE)
    postalCode = models.CharField(blank=True, max_length=70)
    post = models.ManyToManyField(eduRole,blank=True,)
    address1 = models.TextField(blank=True)
    address2 = models.TextField(blank=True)
    religion = models.CharField(max_length=120,blank=True)
    demicile = models.CharField(max_length=100,blank=True)
    provence = models.CharField(max_length=120,blank=True)
    city = models.CharField(max_length=120,blank=True)
    Districe = models.CharField(max_length=120,blank=True)
    Tehsil = models.CharField(max_length=120,blank=True)
    anyHonorsAwards = models.TextField(blank=True)
    dateOfapplyed = models.DateTimeField(default=timezone.now,editable=False)
    cv = models.FileField(upload_to=upload_path,blank=True)
    is_staff = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS_CHOICES, default=PENDING, max_length=20)

    def pathnm(self):
        return str(f"cv_{self.userS}")

    def __str__(self):
        return str(self.userS)

class eduStudents(models.Model):
    edu = models.ForeignKey(xEduInstitution , on_delete=models.CASCADE) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dataForm = models.ForeignKey(studentAdmitForm, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    eduID = models.CharField(max_length=50,null=True,blank=True)
    joinedAt = models.DateField(default=timezone.now,editable=False)
    disable = models.BooleanField(default=False)
    ex_Student = models.BooleanField(default=False)
    equiet = models.BooleanField(default=False)
    suspend = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.user:
            self.eduID = str(f"student_{str(self.edu)}{self.user}{str(self.uuid)[:5]}").replace(" ", "")
            super().save(*args, **kwargs)
        if self.disable:
            self.ex_Student = True
            super().save(*args, **kwargs)

    def __str__(self):
        return str(f"{self.eduID}")
    
class eduFaculty(models.Model):
    edu = models.ForeignKey(xEduInstitution , on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dataForm = models.ForeignKey(jobCvForm, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    eduID = models.CharField(max_length=50,null=True,blank=True)
    joinedAt = models.DateField(default=timezone.now,editable=False)
    disable = models.BooleanField(default=False)
    ex_Faculty = models.BooleanField(default=False)
    equiet = models.BooleanField(default=False)
    suspend = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.user:
            self.eduID = str(f"staff_{str(self.edu)}{self.user}{str(self.uuid)[:5]}").replace(" ", "")
            super().save(*args, **kwargs)
        if self.disable:
            self.ex_Faculty = True
            super().save(*args, **kwargs)
        

    def __str__(self):
        return str(f"{self.user} | {self.user.get_full_name()}")
    
class EduMember(models.Model):
    edu = models.ForeignKey(xEduInstitution , on_delete=models.CASCADE)
    eduStudent = models.ForeignKey(studentAdmitForm,null=True,blank=True, on_delete=models.CASCADE)
    eduemployees = models.ForeignKey(jobCvForm,null=True,blank=True, on_delete=models.CASCADE)
    group = models.ManyToManyField(Group)
    eduID = models.CharField(max_length=50,null=True,blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    dateOfReg = models.DateField(default=timezone.now,editable=False)

    def save(self, *args, **kwargs):
        if self.eduStudent:
            self.eduID = str(f"st_{str(self.edu)}{self.eduStudent}{str(self.uuid)[:5]}").replace(" ", "")
            super().save(*args, **kwargs)
        elif self.eduemployees:
            self.eduID = str(f"flt_{self.edu}{self.eduemployees}{str(self.uuid)[:5]}").replace(" ", "")
            super().save(*args, **kwargs)

    def __str__(self):
        return str(f"{self.eduID}")
    