# Generated by Django 5.0.1 on 2024-04-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dbDoctors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appoiment",
            name="patient_phone",
            field=models.CharField(max_length=15),
        ),
    ]
