from django.shortcuts import render
from django.http import HttpResponse
from  .models import Travels
from datetime import datetime


def home(request):
    return render(request,'travel/home.html', {'title': 'Home'})

def about(request):
    return HttpResponse('<h1>About</h1>')

def travel(request):
    if request.method == 'POST':  
        print (request.POST["travelon"])
        print (request.POST["returnon"])
        d0 =  datetime.strptime(request.POST["travelon"], "%d/%m/%Y").date()
        d1 = datetime.strptime(request.POST["returnon"], "%d/%m/%Y").date()
    
        diff = d1 - d0
        print(diff.days)
        context = {
            'travels': Travels.objects.filter(destination=request.POST["dest"]).filter(ageFrom__lte=request.POST["age"]).filter(ageTo__gt=request.POST["age"]).filter(dayFrom__lte=diff.days).filter(dayTo__gt=diff.days),
            'title' :'Travel',
            'period':diff.days}
    return render(request, 'travel/travel.html', context)
       

    
def travelform(request):
    return render(request,'travel/travelform.html', {'title': 'Travel'})