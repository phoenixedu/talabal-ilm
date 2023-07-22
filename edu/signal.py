from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from edu.models import InstCourse,Semester
from django.core.exceptions import ValidationError


@receiver(post_save, sender=Semester)
def update_smFull(sender, instance, **kwargs):
    course = instance.course
    existing_semesters = Semester.objects.filter(course_id=course.id).count()
    if existing_semesters >= course.totalSimsters:
        course.smFull = True
    else:
        course.smFull = False
    course.save()
    

@receiver(pre_save, sender=InstCourse)
def update_smFull_on_totalSimsters_change(sender, instance, **kwargs):
    if instance.id:
        try:
            existing_instance = InstCourse.objects.get(id=instance.id)
            if existing_instance.totalSimsters <= instance.totalSimsters:
                instance.smFull = False
            else:
                if (
                    existing_instance.totalSimsters is not None
                    and instance.totalSimsters is not None
                    and instance.totalSimsters < existing_instance.totalSimsters
                ):
                    raise ValidationError("Cannot decrease the totalSimsters value.")
        except InstCourse.DoesNotExist:
            pass
        

            
