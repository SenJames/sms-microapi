# Generated by Django 3.0.7 on 2020-07-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='dateScheduled',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='senderdetails',
            name='sid',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
    ]