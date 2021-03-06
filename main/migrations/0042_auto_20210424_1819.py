# Generated by Django 3.1.7 on 2021-04-24 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20210423_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientencounter',
            name='chief_complaint',
            field=models.ManyToManyField(blank=True, null=True, to='main.ChiefComplaint'),
        ),
        migrations.AlterField(
            model_name='patientencounter',
            name='diagnoses',
            field=models.ManyToManyField(blank=True, null=True, to='main.Diagnosis'),
        ),
        migrations.AlterField(
            model_name='patientencounter',
            name='treatments',
            field=models.ManyToManyField(blank=True, null=True, to='main.Treatment'),
        ),
    ]
