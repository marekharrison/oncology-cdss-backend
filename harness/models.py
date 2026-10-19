from django.db import models

class Patient(models.Model):
    patient_num = models.IntegerField(null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    psa_level = models.DecimalField(max_digits=8, decimal_places=4)
    gleason_score = models.IntegerField(null=True)
    clinical_stage = models.CharField(max_length=255)
