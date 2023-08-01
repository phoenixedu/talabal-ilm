from django.db import models
from edu_stracture.models import eduClass
from edu_members.models import eduFaculty,eduStudents
from django.utils import timezone
import os 
import random
import uuid
# Create your models here.


def upload_notes(instance, filename):
    ext = filename.split('.')[-1]
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    filename = f'Lecture_notes_{instance.title}-{instance.lecture}-{random_numbers}.{ext}'
    return os.path.join('docment/lecture_notes', filename)

def upload_thumbnail(instance, filename):
    ext = filename.split('.')[-1]
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    filename = f'thumb_{instance.uuid}-{random_numbers}.{ext}'
    return os.path.join('images/videos_thumbnail', filename)

def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    filename = f'viddeo_{instance.uuid}-{random_numbers}.{ext}'
    return os.path.join('videos/electure', filename)

class ClassOfStudents(models.Model):
    Eclass = models.ForeignKey(eduClass, on_delete=models.CASCADE,related_name="online_class_edu_class")
    name = models.CharField(default="A",max_length=50)
    incharge = models.ForeignKey(
        eduFaculty,
        on_delete=models.CASCADE,
        related_name='classes_in_charge'
    )
    studentsOfclass = models.ManyToManyField(
        eduStudents,
        blank=True,
        related_name='class_student'
    )
    createDateTime = models.DateTimeField(default=timezone.now,editable=False)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    cls_key = models.CharField(null=True,max_length=50)
    def save(self, *args, **kwargs):
        self.nameKy = self.name.replace(" ", "")
        classx  = str(self.Eclass)
        self.clsD = classx.replace("|","").replace(" ","")
        self.cls_key = f"{self.nameKy}{self.clsD}{str(self.uuid)[:10]}"
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.name} | {self.Eclass}'
    

class eClassVideos(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    thumbnail = models.FileField(upload_to=upload_thumbnail,blank=True, null=True)
    video = models.FileField(upload_to=upload_path,blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    upLoadDate = models.DateTimeField(default=timezone.now,editable=False)

    def __str__(self):
        return self.name


class Electure(models.Model):
    Eclass = models.ForeignKey(ClassOfStudents, on_delete=models.CASCADE,related_name='lectures')
    teacher  = models.ForeignKey(
            eduFaculty,
            on_delete=models.CASCADE,
            related_name='class_taker'
        )
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    video = models.ForeignKey(eClassVideos,on_delete=models.SET_NULL,blank=True,null=True)
    over = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)
    def count_attendance(self):
        total_students = self.Eclass.studentsOfclass.count()
        attended_students = self.attendance_set.filter(is_present=True).count()
        absent_students = total_students - attended_students
        return attended_students, absent_students
    
    def __str__(self):
        return str(f'{self.Eclass} | {self.teacher}')

class Attendance(models.Model):
    lecture = models.ForeignKey(Electure, on_delete=models.CASCADE)
    student = models.ForeignKey(
        ClassOfStudents,
        on_delete=models.CASCADE,
        related_name="student_att",
        limit_choices_to={'studentsOfclass__gte': 1}
        )  
    is_present = models.BooleanField(default=False)
    on_leave = models.BooleanField(default=False)
    attendance_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('lecture', 'student')

class electureNotes(models.Model):
    lecture = models.ForeignKey(Electure, on_delete=models.CASCADE , related_name="electure_notes")
    title = models.CharField(max_length=150)
    notes = models.FileField(upload_to=upload_notes,null=True,blank=True)
    dateOfUplaoding = models.DateTimeField(default=timezone.now,editable=False)

    def __str__(self):
        return self.title
    