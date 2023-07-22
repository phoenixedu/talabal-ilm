from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,User
from django.utils import timezone
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
import uuid
import random 
import os

def upload_path(instance, filename):
    """Generate a new filename for the uploaded file"""
    ext = filename.split('.')[-1]  # get the file extension
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    filename = f'{instance.username}-{instance.uuid}-{random_numbers}.{ext}'
    return os.path.join('images/genUserProfile', filename)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class GenUser(AbstractBaseUser, PermissionsMixin):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,null=True, blank=True,)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    father_name = models.CharField(max_length=255)
    PhoneNumber = models.CharField(blank=True,null=True,max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    picture = models.ImageField(upload_to=upload_path, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    cnic = models.CharField(max_length=15,unique=True)
    DOB = models.DateField()
    country = CountryField()
    sex = models.CharField(max_length=10,choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    join_date = models.DateTimeField(default=timezone.now , editable=False)
    pk_key = models.CharField(max_length=255, unique=True)

    # token
    email_verification_token = models.CharField(max_length=255, null=True, blank=True)
    # conformations
    emailConformation = models.BooleanField(default=False)
    PhoneNumberConformation = models.BooleanField(default=False)
    PaidMember = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
    def save(self, *args, **kwargs):
        self.pk_key = self.username + str(self.uuid)[:5]
        super().save(*args, **kwargs)
    @property
    def age(self):
        today = date.today()
        age = today.year - self.DOB.year
        if today.month < self.DOB.month or (today.month == self.DOB.month and today.day < self.DOB.day):
            age -= 1
            if age <= 0:
                age = 0
        return age
    def get_full_name(self):
        if self.last_name == None:
            return f'{self.first_name}'
        elif self.last_name and self.first_name :
           return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.username}'
 
    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    # Add relateive name arguments to resolve the clash
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_users', blank=True)