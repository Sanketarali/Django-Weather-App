from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='indore'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6486a4c3efa3cef9c963837111794363'
    PARAMS={'units':'metric'}

    data=requests.get(url,PARAMS).json()
    description=data['weather'][0]['description']
    icon=data['weather'][0]['icon']
    temp=data['main']['temp']

    day=datetime.date.today()

    return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})