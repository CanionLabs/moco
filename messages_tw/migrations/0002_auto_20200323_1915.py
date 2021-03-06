# Generated by Django 2.2.6 on 2020-03-23 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_tw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='has_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='has_error',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='kind',
            field=models.CharField(choices=[('whatsapp', 'Whatsapp'), ('sms', 'SMS')], default='Whatsapp', max_length=15),
            preserve_default=False,
        ),
    ]
