# Generated by Django 4.0.5 on 2023-08-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_permissions', '0005_alter_groupofsubheadofinstetude_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inchargeofclass',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
