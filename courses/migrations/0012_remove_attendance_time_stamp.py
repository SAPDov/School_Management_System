# Generated by Django 3.2.7 on 2021-09-19 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20210919_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='time_stamp',
        ),
    ]