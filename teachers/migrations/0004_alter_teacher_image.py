# Generated by Django 3.2.7 on 2021-09-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]