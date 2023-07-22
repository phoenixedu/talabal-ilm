# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import HeadOfTheDepartment, GroupOfAdmins, GroupOfSubHeadOfInstetude, GroupOfStudents, GroupOfTeachers, InchargeOfClass, HeadOfInstetude

# def update_head_status(sender, instance, **kwargs):
#     post_save.disconnect(update_head_status, sender=sender)
    
#     edu = instance.edu
#     head = sender.objects.get(edu=edu)
#     headCount = head.members.count()
#     head.is_full = headCount >= head.capacity
#     head.save()

#     post_save.connect(update_head_status, sender=sender)

# # Connect the signal handler to all the relevant models
# @receiver(post_save, sender=HeadOfTheDepartment)
# @receiver(post_save, sender=GroupOfAdmins)
# @receiver(post_save, sender=GroupOfStudents)
# @receiver(post_save, sender=GroupOfTeachers)
# @receiver(post_save, sender=InchargeOfClass)
# @receiver(post_save, sender=GroupOfSubHeadOfInstetude)
# def head_signal(sender, instance, **kwargs):
#     update_head_status(sender, instance, **kwargs)


# from django.db.models.signals import post_save,pre_save
# from django.dispatch import receiver
# from .models import HeadOfTheDepartment,GroupOfAdmins,GroupOfSubHeadOfInstetude,GroupOfStudents,GroupOfTeachers,InchargeOfClass,HeadOfInstetude
# from django.core.exceptions import ValidationError


# @receiver(post_save, sender=HeadOfInstetude)
# def head_signal(sender, instance, **kwargs):
    
#     post_save.disconnect(head_signal, sender=HeadOfInstetude)
#     edu = instance.edu
#     heads = HeadOfInstetude.objects.get(edu=edu)
#     headCount = heads.members.count()
#     if headCount >= heads.capacity:
#         heads.is_full = True
#     else:
#         heads.is_full = False
#     heads.save()
    
#     post_save.connect(head_signal, sender=HeadOfInstetude)


# @receiver(post_save, sender=HeadOfTheDepartment)
# def head_signal(sender, instance, **kwargs):
    
#     post_save.disconnect(head_signal, sender=HeadOfTheDepartment)
#     edu = instance.edu
#     heads = HeadOfTheDepartment.objects.get(edu=edu)
#     headCount = heads.members.count()
#     if headCount >= heads.capacity:
#         heads.is_full = True
#     else:
#         heads.is_full = False
#     heads.save()
    
#     post_save.connect(head_signal, sender=HeadOfTheDepartment)


# @receiver(post_save, sender=GroupOfAdmins)
# def head_signal(sender, instance, **kwargs):
    
#     post_save.disconnect(head_signal, sender=GroupOfAdmins)
#     edu = instance.edu
#     heads = GroupOfAdmins.objects.get(edu=edu)
#     headCount = heads.members.count()
#     if headCount >= heads.capacity:
#         heads.is_full = True
#     else:
#         heads.is_full = False
#     heads.save()
    
#     post_save.connect(head_signal, sender=GroupOfAdmins)


# @receiver(post_save, sender=GroupOfStudents)
# def head_signal(sender, instance, **kwargs):
    
#     post_save.disconnect(head_signal, sender=GroupOfStudents)
#     edu = instance.edu
#     heads = GroupOfStudents.objects.get(edu=edu)
#     headCount = heads.members.count()
#     if headCount >= heads.capacity:
#         heads.is_full = True
#     else:
#         heads.is_full = False
#     heads.save()
    
#     post_save.connect(head_signal, sender=GroupOfStudents)


# @receiver(post_save, sender=GroupOfTeachers)
# def head_signal(sender, instance, **kwargs):
    
#     post_save.disconnect(head_signal, sender=GroupOfTeachers)
#     edu = instance.edu
#     heads = GroupOfTeachers.objects.get(edu=edu)
#     headCount = heads.members.count()
#     if headCount >= heads.capacity:
#         heads.is_full = True
#     else:
#         heads.is_full = False
#     heads.save()
    
#     post_save.connect(head_signal, sender=GroupOfTeachers)


# @receiver(post_save, sender=InchargeOfClass)
# def head_signal(sender, instance, **kwargs):
    
#     post_save.disconnect(head_signal, sender=InchargeOfClass)
#     edu = instance.edu
#     heads = InchargeOfClass.objects.get(edu=edu)
#     headCount = heads.members.count()
#     if headCount >= heads.capacity:
#         heads.is_full = True
#     else:
#         heads.is_full = False
#     heads.save()
    
#     post_save.connect(head_signal, sender=InchargeOfClass)


# @receiver(post_save, sender=GroupOfSubHeadOfInstetude)
# def head_signal(sender, instance, **kwargs):
    
#     post_save.disconnect(head_signal, sender=GroupOfSubHeadOfInstetude)
#     edu = instance.edu
#     heads = GroupOfSubHeadOfInstetude.objects.get(edu=edu)
#     headCount = heads.members.count()
#     if headCount >= heads.capacity:
#         heads.is_full = True
#     else:
#         heads.is_full = False
#     heads.save()
    
#     post_save.connect(head_signal, sender=GroupOfSubHeadOfInstetude)