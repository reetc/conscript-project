# Generated by Django 2.0.1 on 2018-10-25 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20181026_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_details',
            name='compId',
        ),
        migrations.AddField(
            model_name='job_details',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='company.Company_details'),
            preserve_default=False,
        ),
    ]
