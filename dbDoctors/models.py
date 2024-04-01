from django.db import models

class Appoiment(models.Model):
    doctor_name = models.CharField(max_length=80)
    date_appoiment = models.DateField()
    time_appoiment = models.TimeField()
    patient_name = models.CharField(max_length=80)
    patient_phone = models.IntegerField()
    reason_for_visit = models.TextField(max_length=400)


class Doctors(models.Model):
    pass