# Generated by Django 2.1.1 on 2018-11-29 13:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_auto_20181129_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotion_output',
            name='emo_output',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]