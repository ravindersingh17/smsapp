# Generated by Django 2.2.2 on 2019-06-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sms',
            name='device_id',
            field=models.CharField(default='', max_length=10),
        ),
    ]