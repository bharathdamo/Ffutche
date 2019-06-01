# Generated by Django 2.1.3 on 2019-03-08 23:27

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eren', '0024_auto_20190308_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificatex',
            name='cer_id',
        ),
        migrations.AddField(
            model_name='certificatex',
            name='cert_page_number',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='certificatex',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]