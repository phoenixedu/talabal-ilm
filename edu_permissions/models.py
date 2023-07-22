from django.db import models
from edu.models import xEduInstitution
from edu_members.models import eduFaculty,eduStudents
from edu_stracture.models import eduDepartment
from edu_onLine_class.models import ClassOfStudents
from django.contrib.auth.models import User
# Create your models here.
class GroupOfTeachers(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE, related_name='group_of_teachers')
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Teacher Groups"
        )
    members = models.ManyToManyField(eduFaculty, blank=True,related_name='teacher_of_edu')
    capacity = models.IntegerField(default=1)
    last_update = models.DateTimeField(auto_now=True)
    is_full = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class GroupOfAdmins(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE, related_name='group_of_admins')
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Admin Group"
        )
    members = models.ManyToManyField(eduFaculty, blank=True,related_name='admin_of_edu')
    capacity = models.IntegerField(default=1)
    last_update = models.DateTimeField(auto_now=True)
    is_full = models.BooleanField(default=False)
    def is_capacity_reached(self):
        if self.members.count() == self.capacity:
            self.is_full=True
    def __str__(self):
        return self.name


class GroupOfStudents(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE, related_name='group_of_students')
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Student Group"
        )
    members = models.ManyToManyField(eduStudents, blank=True,related_name="student_of_edu")
    capacity = models.IntegerField(default=20)
    last_update = models.DateTimeField(auto_now=True)
    is_full = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class HeadOfTheDepartment(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE,related_name="GroupOfHeadOfDeparment")
    department = models.ForeignKey(eduDepartment, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Head Of the Department"
        )
    members = models.ManyToManyField(eduFaculty, blank=True,related_name="head_of_the_department")
    capacity = models.IntegerField(default=1)
    last_update = models.DateTimeField(auto_now=True)
    is_full = models.BooleanField(default=False)
   

    def __str__(self):
        return self.name
    
class InchargeOfClass(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE,related_name="InchargeOfClassGroup")
    department = models.ForeignKey(eduDepartment, on_delete=models.CASCADE)
    Eclass = models.ForeignKey(ClassOfStudents,on_delete=models.CASCADE,related_name='InchargeOfEclass')
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Class Incharge"
        )
    members = models.ManyToManyField(GroupOfTeachers, blank=True,related_name="incharge_of_class")
    capacity = models.IntegerField(default=1)
    last_update = models.DateTimeField(auto_now=True)
    is_full = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class HeadOfInstetude(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE,related_name="HeadOfInstetude")
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Head Of Instetude"
        )
    members = models.ManyToManyField(User, blank=True,related_name="head_of_instetude")
    capacity = models.IntegerField(default=1)
    last_update = models.DateTimeField(auto_now=True)
    is_full = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class GroupOfSubHeadOfInstetude(models.Model):
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE,related_name="GroupOfSubHeadOfInstetude")
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default="Sub-head Of Instetude"
        )
    members = models.ManyToManyField(User, blank=True,related_name="sub_head_of_instetude")
    capacity = models.IntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)
    is_full = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name