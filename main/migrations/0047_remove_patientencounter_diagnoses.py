# Generated by Django 3.1.7 on 2021-04-29 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20210428_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientencounter',
            name='diagnoses',
        ),
    ]
