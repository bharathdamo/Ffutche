# Generated by Django 2.1.3 on 2018-12-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=42)),
                ('lastname', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.IntegerField(max_length=15)),
                ('contribution_type', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
