# Generated by Django 5.0.1 on 2024-04-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dbDoctors", "0002_alter_appoiment_patient_phone"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appoiment",
            name="doctor_name",
        ),
        migrations.AddField(
            model_name="appoiment",
            name="doctor_name",
            field=models.ManyToManyField(to="dbDoctors.doctors"),
        ),
    ]
