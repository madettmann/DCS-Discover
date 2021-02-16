from django.db import models

# Create your models here.
class Material(models.Model):
    compound_name = models.CharField(max_length = 100)
    structure_url = models.CharField(max_length = 200, blank = True, null = True)
    iupac_name = models.CharField(max_length = 200)
    mobility = models.FloatField( blank = True, null = True)
    skeletal_formula_file = models.CharField(max_length = 200, blank = True, null = True)
    experimental_data_file = models.CharField(max_length = 200)
    dft_data_file = models.CharField(max_length = 200, blank = True, null = True)
    dftb_data_file = models.CharField(max_length = 200, blank = True, null = True)
    chimes_data_file = models.CharField(max_length = 200, blank = True, null = True)

    def __str__(self):
        return f"{self.compound_name}"