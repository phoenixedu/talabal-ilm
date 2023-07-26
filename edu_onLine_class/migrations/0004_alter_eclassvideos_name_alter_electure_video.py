# Generated by Django 4.2.3 on 2023-07-17 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu_onLine_class', '0003_alter_eclassvideos_name_alter_eclassvideos_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eclassvideos',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='electure',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu_onLine_class.eclassvideos'),
        ),
    ]