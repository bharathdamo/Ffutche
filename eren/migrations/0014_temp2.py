# Generated by Django 2.1.3 on 2019-03-08 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eren', '0013_auto_20190308_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp2',
            fields=[
                ('idd', models.CharField(max_length=42, primary_key=True, serialize=False)),
                ('gg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.tempp')),
            ],
        ),
    ]
