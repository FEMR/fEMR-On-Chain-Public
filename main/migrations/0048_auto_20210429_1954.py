# Generated by Django 3.1.7 on 2021-04-29 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_remove_patientencounter_diagnoses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='administration_schedule',
            field=models.CharField(blank=True, choices=[], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='medication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.medication'),
        ),
    ]
