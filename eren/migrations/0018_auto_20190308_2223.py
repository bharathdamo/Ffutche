# Generated by Django 2.1.3 on 2019-03-08 22:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eren', '0017_certificate_no_generator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate_no_generator',
            name='color',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default='green', max_length=6),
        ),
        migrations.AlterField(
            model_name='certificate_no_generator',
            name='year_code',
            field=models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(100)]),
        ),
    ]
