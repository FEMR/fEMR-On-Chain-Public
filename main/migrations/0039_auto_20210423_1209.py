# Generated by Django 3.1.8 on 2021-04-23 16:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_campaign_telehealth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientencounter',
            name='body_temperature',
        ),
        migrations.RemoveField(
            model_name='patientencounter',
            name='diastolic_blood_pressure',
        ),
        migrations.RemoveField(
            model_name='patientencounter',
            name='glucose_level',
        ),
        migrations.RemoveField(
            model_name='patientencounter',
            name='heart_rate',
        ),
        migrations.RemoveField(
            model_name='patientencounter',
            name='mean_arterial_pressure',
        ),
        migrations.RemoveField(
            model_name='patientencounter',
            name='oxygen_concentration',
        ),
        migrations.RemoveField(
            model_name='patientencounter',
            name='respiratory_rate',
        ),
        migrations.RemoveField(
            model_name='patientencounter',
            name='systolic_blood_pressure',
        ),
        migrations.CreateModel(
            name='Vitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diastolic_blood_pressure', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)])),
                ('systolic_blood_pressure', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)])),
                ('mean_arterial_pressure', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('heart_rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(170), django.core.validators.MinValueValidator(40)])),
                ('respiratory_rate', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)])),
                ('body_temperature', models.FloatField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)])),
                ('oxygen_concentration', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(70)])),
                ('glucose_level', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)])),
                ('encounter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.patientencounter')),
            ],
        ),
    ]
