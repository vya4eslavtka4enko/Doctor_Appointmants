from django.shortcuts import render
from .models import Doctors
def main(request):
    list_of_doctors = Doctors.objects.all().values('doctor_name')
    list_of_doctors = [item['doctor_name']for item in list_of_doctors]
    return render(request,'main.html',{'list_of_doctors':list_of_doctors})
