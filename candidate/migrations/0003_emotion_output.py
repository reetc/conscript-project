# Generated by Django 2.1.1 on 2018-11-29 12:10

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_candidate_personal_details_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='emotion_output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('emo_output', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
