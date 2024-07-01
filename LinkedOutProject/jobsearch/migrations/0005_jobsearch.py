# Generated by Django 5.0.6 on 2024-05-16 15:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0004_job_salary_alter_job_job_id_alter_job_pub_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('workplace_type', models.CharField(choices=[('1', 'On-site'), ('2', 'Remote'), ('3', 'Hybrid')], max_length=1)),
                ('level', models.CharField(choices=[('1', 'Internship'), ('2', 'Entry-level'), ('3', 'Associate'), ('4', 'Mid-Senior'), ('5', 'Director'), ('6', 'Executive')], max_length=1)),
                ('recency', models.CharField(choices=[('1', 'Internship'), ('2', 'Entry-level'), ('3', 'Associate'), ('4', 'Mid-Senior'), ('5', 'Director'), ('6', 'Executive')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]