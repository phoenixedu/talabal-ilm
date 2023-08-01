from django.db.models.signals import post_save,pre_save,m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import HeadOfTheDepartment, GroupOfAdmins, GroupOfSubHeadOfInstetude, GroupOfStudents, GroupOfTeachers, InchargeOfClass, HeadOfInstetude
from .GroupsNames import GROUP_OF_INSTETUDE_HEAD,GROUP_OF_HEAD_OF_DEPARTMENT,GROUP_OF_INSTETUDE_SUB_HEADS,GROUP_OF_CLASS_INCHARGE,GROUP_OF_TEACHERS,GROUP_OF_ADMINS,GROUP_OF_STUDENTS

@receiver(post_save, sender=HeadOfInstetude)
def update_smFull(sender, instance, **kwargs):
    if instance.members:
        try:
            group = Group.objects.get(name=GROUP_OF_INSTETUDE_HEAD)
        except:
            group,_ = Group.objects.get_or_create(name=GROUP_OF_INSTETUDE_HEAD)
        group.user_set.clear()
        for faculty in instance.members.all():
            group.user_set.add(faculty.user)

@receiver(post_save, sender=GroupOfTeachers)
def teacherGp_post_save(sender, instance, **kwargs):
    if instance.members:
        try:
            group = Group.objects.get(name=GROUP_OF_TEACHERS)
        except:
            group,_ = Group.objects.get_or_create(name=GROUP_OF_TEACHERS)
        group.user_set.clear()
        for faculty in instance.members.all():
            group.user_set.add(faculty.user)
            
@receiver(post_save, sender=GroupOfAdmins)
def teacherGp_post_save(sender, instance, **kwargs):
    if instance.members:
        try:
            group = Group.objects.get(name=GROUP_OF_ADMINS)
        except:
            group,_ = Group.objects.get_or_create(name=GROUP_OF_ADMINS)
        group.user_set.clear()
        for faculty in instance.members.all():
            group.user_set.add(faculty.user)
           
@receiver(post_save, sender=GroupOfSubHeadOfInstetude)
def teacherGp_post_save(sender, instance, **kwargs):
    if instance.members:
        try:
            group = Group.objects.get(name=GROUP_OF_INSTETUDE_SUB_HEADS)
        except:
            group,_ = Group.objects.get_or_create(name=GROUP_OF_INSTETUDE_SUB_HEADS)
        group.user_set.clear()
        for faculty in instance.members.all():
            group.user_set.add(faculty.user)

@receiver(post_save, sender=HeadOfTheDepartment)
def teacherGp_post_save(sender, instance, **kwargs):
    if instance.members:
        try:
            group = Group.objects.get(name=GROUP_OF_HEAD_OF_DEPARTMENT)
        except:
            group,_ = Group.objects.get_or_create(name=GROUP_OF_HEAD_OF_DEPARTMENT)
        group.user_set.clear()
        for faculty in instance.members.all():
            group.user_set.add(faculty.user)

@receiver(post_save, sender=InchargeOfClass)
def ClsIn_update_smFull(sender, instance, **kwargs):
    print('working...')
    if instance.members:
        try:
            group = Group.objects.get(name=GROUP_OF_CLASS_INCHARGE)
        except:
            group,_ = Group.objects.get_or_create(name=GROUP_OF_CLASS_INCHARGE)
        group.user_set.clear()
        for faculty in instance.members.all():
            group.user_set.add(faculty.user)
            print(f'{faculty.user} added to {group}')
        
@receiver(post_save, sender=GroupOfStudents)
def teacherGp_post_save(sender, instance, **kwargs):
    if instance.members:
        try:
            group = Group.objects.get(name=GROUP_OF_STUDENTS)
        except:
            group,_ = Group.objects.get_or_create(name=GROUP_OF_STUDENTS)
        group.user_set.clear()
        for Student in instance.members.all():
            group.user_set.add(Student.user)


            