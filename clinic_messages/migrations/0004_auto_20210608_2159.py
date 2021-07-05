# Generated by Django 3.2.4 on 2021-06-09 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_messages', '0003_alter_message_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='deleted_by_recipient',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='message',
            name='deleted_by_sender',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]