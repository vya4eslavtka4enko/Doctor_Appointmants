from django.shortcuts import render
from .models import Doctors,Appoiment
from .forms import AppoimentForm
from django.http import HttpResponseRedirect
def main(request):
    list_of_doctors = Doctors.objects.all().values('doctor_name')
    list_of_doctors = [item['doctor_name']for item in list_of_doctors]

    doctor_name=''
    date_appoiment=''
    time_appoiment=''
    name=''
    phone=''
    reason=''
    form = ''
    if request.method == 'POST':
            doctor_name = request.POST.get('doctor_name')
            date_appoiment = request.POST.get('date')
            time_appoiment = request.POST.get('time')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            reason = request.POST.get('reason')

            patient = AppoimentForm()
            patient.doctor_name=doctor_name
            patient.date_appoiment=date_appoiment
            patient.time_appoiment=time_appoiment
            patient.patient_name=name
            patient.patient_phone=phone
            patient.reason_for_visit=reason


    return render(request,'main.html',{'list_of_doctors':list_of_doctors,})
