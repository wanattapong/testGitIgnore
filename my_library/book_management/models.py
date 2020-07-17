from django.db import models

# Create your models here.
class Form_Diposit(models.Model):
    originalcode = models.CharField(max_length=255, null=False, blank=True, unique=True)
    phylum = models.CharField(max_length=255, null=True, blank=True)
    order = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.originalcode