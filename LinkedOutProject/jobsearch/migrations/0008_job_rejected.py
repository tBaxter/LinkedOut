# Generated by Django 5.0.6 on 2024-05-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0007_job_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]