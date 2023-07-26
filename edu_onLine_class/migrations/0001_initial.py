# Generated by Django 4.2.3 on 2023-07-16 15:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import edu_onLine_class.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('edu_stracture', '0001_initial'),
        ('edu_members', '0004_edufaculty_equiet_edufaculty_suspend_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassOfStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='A', max_length=50)),
                ('createDateTime', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('cls_key', models.CharField(max_length=50, null=True)),
                ('Eclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu_stracture.educlass')),
                ('incharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes_in_charge', to='edu_members.edufaculty')),
                ('studentsOfclass', models.ManyToManyField(blank=True, related_name='class_student', to='edu_members.edustudents')),
            ],
        ),
        migrations.CreateModel(
            name='eClassVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('thumbnail', models.FileField(upload_to=edu_onLine_class.models.upload_thumbnail)),
                ('video', models.FileField(upload_to=edu_onLine_class.models.upload_path)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('upLoadDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Electure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('over', models.BooleanField(default=False)),
                ('cancel', models.BooleanField(default=False)),
                ('Eclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='edu_onLine_class.classofstudents')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_taker', to='edu_members.edufaculty')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu_onLine_class.eclassvideos')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=False)),
                ('attendance_time', models.DateTimeField(blank=True, null=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu_onLine_class.electure')),
                ('student', models.ForeignKey(limit_choices_to={'studentsOfclass__gte': 1}, on_delete=django.db.models.deletion.CASCADE, to='edu_onLine_class.classofstudents')),
            ],
            options={
                'unique_together': {('lecture', 'student')},
            },
        ),
    ]