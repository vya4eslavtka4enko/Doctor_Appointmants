from django.shortcuts import render

def main(request):
    print('1')
    return render(request,'main.html')
