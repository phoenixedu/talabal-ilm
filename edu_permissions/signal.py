from django.db.models.signals import post_save,pre_save,m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import HeadOfTheDepartment, GroupOfAdmins, GroupOfSubHeadOfInstetude, GroupOfStudents, GroupOfTeachers, InchargeOfClass, HeadOfInstetude
from .GroupsNames import GROUP_OF_INSTETUDE_HEAD

@receiver(post_save, sender=HeadOfInstetude)
def update_smFull(sender, instance, **kwargs):
    if instance.edu:
        edu = instance.edu
        try:
            head = HeadOfInstetude.objects.get(edu=edu)
            coutHead = head.members.count()
            if coutHead < head.capacity:
                head.is_full = False
            elif coutHead >= head.capacity:
                head.is_full = True
            else:
                head.is_full = False
            head.save()
        except:
            pass
    if instance.members:
        try:
            head_group = Group.objects.get(name=GROUP_OF_INSTETUDE_HEAD)
        except:
            head_group,_ = Group.objects.get_or_create(name=GROUP_OF_INSTETUDE_HEAD)
        for member in head.members.all():
            if member:
                head_group.user_set.add(member)


    