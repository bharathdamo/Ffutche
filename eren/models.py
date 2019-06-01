from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class donations(models.Model):
    firstname = models.CharField(max_length=42)
    lastname = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    # phone = models.IntegerField()
    phone = models.CharField(max_length=42)
    contribution_type = models.CharField(max_length=255)
    amount  = models.PositiveIntegerField()
    time = models.DateTimeField(auto_now_add=True)

    # slug = models.SlugField(unique=True, max_length=255)
    # content = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)
    # author = models.TextField()

#
# class client(models.Model):
#     client_name = models.CharField(max_length=42, primary_key=True)
#     client_type = models.CharField(max_length=42, blank = True)
#
#
# class user(models.Model):
#     client_id = models.ForeignKey(client, on_delete=models.SET_NULL, null=True)
#     first_name = models.CharField(max_length=42)
#     middle_name = models.CharField(max_length=42, blank = True)
#     last_name = models.CharField(max_length=42)
#     job_title = models.CharField(max_length=42, blank = True)
#     email = models.CharField(max_length=42, primary_key=True)
#     office_phone = models.IntegerField(blank = True)
#     cell_phone = models.IntegerField(blank = True)
#     password = models.CharField(max_length=42, blank = True)
#     prefix = models.CharField(max_length=42, blank = True)
#
# class location(models.Model):
#     id = models.CharField(max_length=50, primary_key=True)
#     client_id = models.ForeignKey(client, on_delete=models.SET_NULL, null=True)
#     address1 = models.CharField(max_length=42, blank = True)
#     address2 = models.CharField(max_length=42, blank = True)
#     city = models.CharField(max_length=42, blank = True)
#     state = models.CharField(max_length=42, blank = True)
#     country = models.CharField(max_length=42, blank = True)
#     zip = models.CharField(max_length=42, blank = True)
#     country = models.CharField(max_length=42, blank = True)
#     phone = models.IntegerField(blank = True)
#     fax =  models.IntegerField(blank = True)
#
#
# class test_standard(models.Model):
#     test_name = models.CharField(max_length=42, primary_key=True)
#     test_description = models.CharField(max_length=42, blank = True)
#     publish_date = models.CharField(max_length=42, blank=True)
#
# class service(models.Model):
#     service_name = models.CharField(max_length=42, primary_key=True)
#     service_description = models.CharField(max_length=42, blank = True)
#     fi_required = models.CharField(max_length=42, blank=True)
#     fi_frequency = models.CharField(max_length=42, blank=True)
#     test_standard = models.ForeignKey(test_standard, on_delete=models.SET_NULL, null=True)
#
#
# class product(models.Model):
#     prod_id = models.CharField(max_length=42, primary_key=True)
#     model_no = models.CharField(max_length=42)
#     name = models.CharField(max_length=42, blank=True)
#     type = models.CharField(max_length=42, blank=True)
#     fireclass = models.CharField(max_length=42, blank=True)
#     length = models.CharField(max_length=42, blank=True)
#     weight = models.CharField(max_length=42, blank=True)
#     individual_cell_area = models.CharField(max_length=42, blank=True)
#     cell_technology = models.CharField(max_length=42, blank=True)
#     cell_manufacturer = models.CharField(max_length=42, blank=True)
#     cell_part_no = models.CharField(max_length=42, blank=True)
#     cell_manufacturer_location = models.CharField(max_length=42, blank=True)
#     total_number_of_cells = models.CharField(max_length=42, blank=True)
#     no_of_cells_in_series = models.CharField(max_length=42, blank=True)
#     number_of_series_strings = models.CharField(max_length=42, blank=True)
#
#     number_of_bypass_diodes = models.CharField(max_length=42, blank=True)
#     bypass_diode_rating = models.CharField(max_length=42, blank=True)
#     bypass_diode_max_temp = models.CharField(max_length=42, blank=True)
#     series_fuse_rating = models.CharField(max_length=42, blank=True)
#     interconnect_material_and_material_contact_number = models.CharField(max_length=42, blank=True)
#     interconnect_dimensions = models.CharField(max_length=42, blank=True)
#     superstrate_type = models.CharField(max_length=42, blank=True)
#     supersrtate_manufacturer_and_part_no = models.CharField(max_length=42, blank=True)
#     substrate_type = models.CharField(max_length=42, blank=True)
#     subsrtate_manufacturer_and_part_no = models.CharField(max_length=42, blank=True)
#
#     frame_type_or_material = models.CharField(max_length=42, blank=True)
#     frame_adhesive = models.CharField(max_length=42, blank=True)
#     encapsulant_type = models.CharField(max_length=42, blank=True)
#     encapsulant_manufacturer_and_part_no = models.CharField(max_length=42, blank=True)
#     junction_box_type = models.CharField(max_length=42, blank=True)
#     junction_box_manufacturer_and_part_no = models.CharField(max_length=42, blank=True)
#     junction_box_potting_material = models.CharField(max_length=42, blank=True)
#     junction_box_adhesive = models.CharField(max_length=42, blank=True)
#     junction_box_use_with_contuit = models.CharField(max_length=42, blank=True)
#     cable_connector_type = models.CharField(max_length=42, blank=True)
#
#
#
#
# class sequence(models.Model):
#     sequence_id = models.CharField(max_length=42, primary_key=True)
#     sequence_name = models.CharField(max_length=100, blank=True)
#
#
#
# class performance(models.Model):
#     performance_id = models.CharField(max_length=42, primary_key=True)
#     model_num = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
#     sequenc_id = models.ForeignKey(sequence, on_delete=models.SET_NULL, null=True)
#     max_system_voltage = models.CharField(max_length=42, blank=True)
#     name = models.CharField(max_length=42, blank=True)
#     open_circuit_voltage = models.CharField(max_length=42, blank=True)
#     short_circuit_current = models.CharField(max_length=42, blank=True)
#     voltage_at_max_power = models.CharField(max_length=42, blank=True)
#     current_at_max_power = models.CharField(max_length=42, blank=True)
#     max_power_output = models.CharField(max_length=42, blank=True)
#     fill_factor = models.CharField(max_length=42, blank=True)
#
#
# class product_factory(models.Model):
#     id = models.CharField(max_length=42, primary_key=True)
#     loc = models.ForeignKey(location, on_delete=models.SET_NULL, null=True)
#     product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
#     contact = models.CharField(max_length=42, blank=True)
#
# class factory_inspection(models.Model):
#     report_no = models.CharField(max_length=42, primary_key=True)
#     locatio_id = models.ForeignKey(location, on_delete=models.SET_NULL, null=True)
#     date = models.CharField(max_length=42, blank=True)
#     inspector = models.CharField(max_length=42, blank=True)
#     inspection_sequence = models.CharField(max_length=42, blank=True)
#     findings = models.CharField(max_length=42, blank=True)
#
# class certificategenerator(models.Model):
#     class Meta:
#         unique_together = (('cert_type_code', 'subsidiary_code','year_code','pv_type_code',"seq"),)
#
#     seq = models.IntegerField(default=1000)
#     cert_type_code =  models.CharField(max_length=2, blank=True)
#     subsidiary_code = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
#     year_code = models.IntegerField(default=100, validators=[MaxValueValidator(999), MinValueValidator(100)])
#     pv_type_code = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
#     def save(self, *args, **kwargs):
#         # This means that the model isn't saved to the database yet
#         if self._state.adding:
#             # Get the maximum display_id value from the database
#             seq = certificategenerator.objects.all().aggregate(largest=models.Max('seq'))['largest']
#
#             # aggregate can return None! Check it first.
#             # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
#             if seq is not None:
#                 self.seq = seq + 1
#
#         super(certificategenerator, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.cert_type_code+" "+str(self.subsidiary_code)+str(self.year_code)+str(self.pv_type_code)+str(self.seq)
#
#
#
# class certificatez(models.Model):
#     certificate_id = models.AutoField(primary_key=True)
#     cert_no = models.ForeignKey(certificategenerator, on_delete=models.SET_NULL, null=True)
#     client_id = models.ForeignKey(client, on_delete=models.SET_NULL, null=True)
#     locc_id = models.ForeignKey(location, on_delete=models.SET_NULL, null=True)
#     report = models.ForeignKey(factory_inspection, on_delete=models.SET_NULL, null=True)
#     contact_name = models.CharField(max_length=42, blank=True)
#     test_std = models.ForeignKey(test_standard, on_delete=models.SET_NULL, null=True)
#     produc = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
#     issue_date = models.CharField(max_length=42, blank=True)
#     cert_page_number = models.IntegerField(default=10, validators=[MaxValueValidator(9999), MinValueValidator(10)])
#
# class expertise(models.Model):
#     id = models.CharField(max_length=42, primary_key=True)
#     test_sttd = models.ForeignKey(test_standard, on_delete=models.SET_NULL, null=True)
#     certification = models.CharField(max_length=42, blank=True)
#
#
# class tempp(models.Model):
#     class Meta:
#         unique_together = (('x', 'y', 'z','m'),)
#     x = models.CharField(max_length=42)
#     y = models.CharField(max_length=42)
#     z = models.CharField(max_length=42)
#     m = models.IntegerField(default=170)
#
#     def save(self, *args, **kwargs):
#         # This means that the model isn't saved to the database yet
#         if self._state.adding:
#             # Get the maximum display_id value from the database
#             m = tempp.objects.all().aggregate(largest=models.Max('m'))['largest']
#
#             # aggregate can return None! Check it first.
#             # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
#             if m is not None:
#                 self.m = m + 1
#
#         super(tempp, self).save(*args, **kwargs)
#     def __str__(self):
#         return self.x+self.y+self.z+str(self.m)
#
#
# class temp2(models.Model):
#     idd = models.CharField(max_length=42, primary_key=True)
#     gg = models.ForeignKey(tempp, on_delete=models.SET_NULL, null=True)





