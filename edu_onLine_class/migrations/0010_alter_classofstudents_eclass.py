# Generated by Django 4.0.5 on 2023-07-31 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu_stracture', '0001_initial'),
        ('edu_onLine_class', '0009_alter_electurenotes_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classofstudents',
            name='Eclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_class_edu_class', to='edu_stracture.educlass'),
        ),
    ]