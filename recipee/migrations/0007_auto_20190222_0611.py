# Generated by Django 2.0.7 on 2019-02-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipee', '0006_items_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='description',
        ),
        migrations.RemoveField(
            model_name='items',
            name='recipee',
        ),
        migrations.RemoveField(
            model_name='items',
            name='status',
        ),
        migrations.RemoveField(
            model_name='items',
            name='video',
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
