# Generated by Django 5.0.6 on 2024-05-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0009_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='co_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
