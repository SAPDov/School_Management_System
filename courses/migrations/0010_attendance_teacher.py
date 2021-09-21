# Generated by Django 3.2.7 on 2021-09-18 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_teacher_about'),
        ('courses', '0009_remove_attendance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
            preserve_default=False,
        ),
    ]