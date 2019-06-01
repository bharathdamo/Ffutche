# Generated by Django 2.1.3 on 2019-03-02 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eren', '0008_auto_20190302_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('prod_id', models.CharField(max_length=42, primary_key=True, serialize=False)),
                ('model_no', models.CharField(max_length=42)),
                ('name', models.CharField(blank=True, max_length=42)),
                ('type', models.CharField(blank=True, max_length=42)),
                ('fireclass', models.CharField(blank=True, max_length=42)),
                ('length', models.CharField(blank=True, max_length=42)),
                ('weight', models.CharField(blank=True, max_length=42)),
                ('individual_cell_area', models.CharField(blank=True, max_length=42)),
                ('cell_technology', models.CharField(blank=True, max_length=42)),
                ('cell_manufacturer', models.CharField(blank=True, max_length=42)),
                ('cell_part_no', models.CharField(blank=True, max_length=42)),
                ('cell_manufacturer_location', models.CharField(blank=True, max_length=42)),
                ('total_number_of_cells', models.CharField(blank=True, max_length=42)),
                ('no_of_cells_in_series', models.CharField(blank=True, max_length=42)),
                ('number_of_series_strings', models.CharField(blank=True, max_length=42)),
                ('number_of_bypass_diodes', models.CharField(blank=True, max_length=42)),
                ('bypass_diode_rating', models.CharField(blank=True, max_length=42)),
                ('bypass_diode_max_temp', models.CharField(blank=True, max_length=42)),
                ('series_fuse_rating', models.CharField(blank=True, max_length=42)),
                ('interconnect_material_and_material_contact_number', models.CharField(blank=True, max_length=42)),
                ('interconnect_dimensions', models.CharField(blank=True, max_length=42)),
                ('superstrate_type', models.CharField(blank=True, max_length=42)),
                ('supersrtate_manufacturer_and_part_no', models.CharField(blank=True, max_length=42)),
                ('substrate_type', models.CharField(blank=True, max_length=42)),
                ('subsrtate_manufacturer_and_part_no', models.CharField(blank=True, max_length=42)),
                ('frame_type_or_material', models.CharField(blank=True, max_length=42)),
                ('frame_adhesive', models.CharField(blank=True, max_length=42)),
                ('encapsulant_type', models.CharField(blank=True, max_length=42)),
                ('encapsulant_manufacturer_and_part_no', models.CharField(blank=True, max_length=42)),
                ('junction_box_type', models.CharField(blank=True, max_length=42)),
                ('junction_box_manufacturer_and_part_no', models.CharField(blank=True, max_length=42)),
                ('junction_box_potting_material', models.CharField(blank=True, max_length=42)),
                ('junction_box_adhesive', models.CharField(blank=True, max_length=42)),
                ('junction_box_use_with_contuit', models.CharField(blank=True, max_length=42)),
                ('cable_connector_type', models.CharField(blank=True, max_length=42)),
            ],
        ),
    ]
