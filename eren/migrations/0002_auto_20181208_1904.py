# Generated by Django 2.1.3 on 2018-12-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eren', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='phone',
            field=models.CharField(max_length=42),
        ),
    ]
