# Generated by Django 2.1.1 on 2018-10-24 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_auto_20181023_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_application_details',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]