# Generated by Django 4.2.3 on 2023-07-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_alter_xeduinstitution_pk_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instcourse',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]