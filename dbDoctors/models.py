from django.db import models


class Doctors(models.Model):
    doctor_name = models.CharField(max_length=80)
    specialization_doctor = models.CharField(max_length=80)

    def __str__(self):
        return self.doctor_name


class Appoiment(models.Model):
    doctor_name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    date_appoiment = models.DateField()
    time_appoiment = models.TimeField()
    patient_name = models.CharField(max_length=80)
    patient_phone = models.IntegerField()
    reason_for_visit = models.TextField(max_length=400)

    def __str__(self):
        return self.patient_name
