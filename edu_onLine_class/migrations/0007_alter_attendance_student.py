# Generated by Django 4.0.5 on 2023-07-17 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu_onLine_class', '0006_attendance_on_leave_alter_electure_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(limit_choices_to={'studentsOfclass__gte': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='student_att', to='edu_onLine_class.classofstudents'),
        ),
    ]