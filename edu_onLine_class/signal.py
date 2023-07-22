# signals.py
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Electure
from datetime import timedelta

@receiver(pre_save, sender=Electure)
def update_over_status(sender, instance, **kwargs):
    
    now = timezone.now() + timedelta(hours=1)
    now_time = now.time()
    lecture_time = instance.date.time()
    if lecture_time <= now_time:
        instance.over = True
    else:
        instance.over = False
