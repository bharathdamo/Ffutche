# Generated by Django 2.1.3 on 2019-03-02 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eren', '0010_auto_20190302_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('cert_no', models.CharField(max_length=42, primary_key=True, serialize=False)),
                ('contact_name', models.CharField(blank=True, max_length=42)),
                ('issue_date', models.CharField(blank=True, max_length=42)),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.client')),
                ('locc_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.location')),
                ('produc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.product')),
            ],
        ),
        migrations.CreateModel(
            name='expertise',
            fields=[
                ('id', models.CharField(max_length=42, primary_key=True, serialize=False)),
                ('certification', models.CharField(blank=True, max_length=42)),
                ('test_sttd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.test_standard')),
            ],
        ),
        migrations.CreateModel(
            name='factory_inspection',
            fields=[
                ('report_no', models.CharField(max_length=42, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=42)),
                ('inspector', models.CharField(blank=True, max_length=42)),
                ('inspection_sequence', models.CharField(blank=True, max_length=42)),
                ('findings', models.CharField(blank=True, max_length=42)),
                ('locatio_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.location')),
            ],
        ),
        migrations.CreateModel(
            name='product_factory',
            fields=[
                ('id', models.CharField(max_length=42, primary_key=True, serialize=False)),
                ('contact', models.CharField(blank=True, max_length=42)),
                ('loc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.location')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.product')),
            ],
        ),
        migrations.AddField(
            model_name='certificate',
            name='report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.factory_inspection'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='test_std',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eren.test_standard'),
        ),
    ]
