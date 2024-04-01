from django import forms
class AppoimentForm(forms.Form):
    doctor_name = forms.CharField(label="doctor_name",max_length=80)
    date_appoiment = forms.CharField(label="date_appoiment",max_length=80)
    time_appoiment = forms.CharField(label="time_appoiment",max_length=80)
    patient_name = forms.CharField(label="name",max_length=80)
    patient_phone = forms.CharField(label="phone",max_length=15)
    reason_for_visit = forms.CharField(label="reason",max_length=400)