# Generated by Django 2.1.3 on 2019-03-08 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eren', '0021_auto_20190308_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate_no_generator',
            name='pv_type_code',
            field=models.CharField(choices=[('one', 'ONE'), ('two', 'TWO'), ('three', 'THREE'), ('four', 'FOUR'), ('five', 'FIVE')], default=1, max_length=6),
        ),
    ]
