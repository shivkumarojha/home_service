# Generated by Django 4.1.4 on 2022-12-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]
