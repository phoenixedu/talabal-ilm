from django.db import models
from edu_stracture.models import eduRole
from edu.models import InstCourse,xEduInstitution
import os
import random
from django.utils import timezone
# model Area

ONGOING = 'Ongoing'
EXPIRED = 'Expired'

STATUS_CHOICES = (
        (ONGOING, 'Ongoing'),
        (EXPIRED, 'Expired'),
)

def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    filename = f'{instance.section()}-{random_numbers}.{ext}'
    return os.path.join('images/PostersAds', filename)



class AdmissionFrom(models.Model):
    
    name = models.CharField(max_length=50)
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE)
    course = models.ManyToManyField(InstCourse,blank=True)
    requirements = models.TextField(blank=True,null=True)
    sectionStart = models.DateField()
    sectionEnd = models.DateField()
    lastDate = models.DateField()
    seats = models.IntegerField()
    bachno = models.IntegerField()
    dateOfcreation = models.DateField(default=timezone.now,editable=False)
    disable = models.BooleanField(default=False)
    ad = models.ImageField(upload_to=upload_path,blank=True,null=True)
    status = models.CharField(choices=STATUS_CHOICES, default=ONGOING, max_length=20)
    

    def section(self):
        return str(f"admission-{self.name}-{self.lastDate}")
    
    def save(self, *args, **kwargs):
        if self.lastDate < timezone.now().date():
            self.status = 'Expired' 
        super().save(*args, **kwargs)

    def __str__(self):
        return str(f"{self.name} | {self.sectionStart}-{self.sectionEnd}")
    
class jobRecruitry(models.Model):
    name = models.CharField(max_length=50)
    edu = models.ForeignKey(xEduInstitution, on_delete=models.CASCADE)
    forPost = models.ManyToManyField(eduRole,blank=True)
    requirements = models.TextField(blank=True,null=True)
    joining = models.DateField()
    lastDate = models.DateField()
    seats = models.IntegerField()
    dateOfcreation = models.DateField(default=timezone.now,editable=False)
    disable = models.BooleanField(default=False)
    ad = models.ImageField(upload_to=upload_path,blank=True,null=True)
    status = models.CharField(choices=STATUS_CHOICES, default=ONGOING, max_length=20)
    
    def section(self):
        return str(f"job-{self.name}-{self.lastDate}")
    
    def save(self, *args, **kwargs):
        if self.lastDate < timezone.now().date():
            self.status = 'Expired' 
        super().save(*args, **kwargs)

    def __str__(self):
        return str(f"{self.name} ")