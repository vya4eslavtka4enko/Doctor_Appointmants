from django.shortcuts import render
from .models import Doctors,Appoiment
from .forms import AppoimentForm
from django.http import HttpResponseRedirect
def main(request):
    list_of_doctors = Doctors.objects.all().values('doctor_name')
    list_of_doctors = [item['doctor_name']for item in list_of_doctors]
    list_of_appoiment = Appoiment.objects.all().values('patient_name','date_appoiment','time_appoiment','doctor_name')
    print(list_of_appoiment)
    doctor_name=''
    date_appoiment=''
    time_appoiment=''
    name=''
    phone=''
    reason=''
    form = ''
    patient=''

    if request.method == 'POST':
            doctor_name = request.POST.get('doctor_name')
            date_appoiment = request.POST.get('date')
            time_appoiment = request.POST.get('time')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            reason = request.POST.get('reason')
            doctors = [Doctors.objects.get(doctor_name=doctor_name) for doc_name in doctor_name]

            appointment = Appoiment.objects.create(
                date_appoiment=date_appoiment,
                time_appoiment=time_appoiment,
                patient_name=name,
                patient_phone=phone,
                reason_for_visit=reason
            )
            appointment.doctor_name.add(*doctors)

            return HttpResponseRedirect('/')

    return render(request,'main.html',{'list_of_doctors':list_of_doctors,
                                                            'list_of_appoiment':list_of_appoiment})
