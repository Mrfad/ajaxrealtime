# Generated by Django 3.2.7 on 2021-09-25 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_rename_scholl_name_user_school_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='sch_name',
            field=models.CharField(max_length=1500, unique=True),
        ),
    ]
