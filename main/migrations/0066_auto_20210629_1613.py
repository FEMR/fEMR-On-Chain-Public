# Generated by Django 3.2.4 on 2021-06-29 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0065_alter_patientencounter_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('photo', models.FileField(blank=True, null=True, upload_to='photos/')),
            ],
        ),
        migrations.AddField(
            model_name='patientencounter',
            name='photos',
            field=models.ManyToManyField(blank=True, to='main.Photo'),
        ),
    ]
