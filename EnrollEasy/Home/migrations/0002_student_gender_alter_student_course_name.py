# Generated by Django 5.0.2 on 2024-03-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Course_Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
