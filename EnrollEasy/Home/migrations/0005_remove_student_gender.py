# Generated by Django 5.0.2 on 2024-03-26 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_student_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Gender',
        ),
    ]
