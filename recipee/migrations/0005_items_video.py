# Generated by Django 2.0.7 on 2018-09-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipee', '0004_auto_20180831_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='video',
            field=models.FileField(default='null', upload_to=''),
        ),
    ]