from django.shortcuts import render, redirect
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.models import User
from django.contrib import auth
from diary.models import Vaccination, Diagnosis

# Create your views here.
def main(request):
    vaccin1 = Vaccination.objects.filter(kind="코로나 장염")
    vaccin2 = Vaccination.objects.filter(kind="종합백신")
    vaccin3 = Vaccination.objects.filter(kind="켄넬 코프")
    vaccin4 = Vaccination.objects.filter(kind="신종플루")
    vaccin5 = Vaccination.objects.filter(kind="광견병")
    sum = 0
    num = 0
    for i in vaccin1:
        sum += i.price
        num += 1
    if num == 0:
        vaccin1 = 0
    else:
        vaccin1 = sum/num

    sum = 0
    num = 0
    for i in vaccin2:
        sum += i.price
        num += 1
    if num == 0:
        vaccin2 = 0
    else:
        vaccin2 = sum/num

    sum = 0
    num = 0
    for i in vaccin3:
        sum += i.price
        num += 1
    if num == 0:
        vaccin3 = 0
    else:
        vaccin3 = sum/num
    

    sum = 0
    num = 0
    for i in vaccin4:
        sum += i.price
        num += 1
    if num == 0:
        vaccin4 = 0
    else:
        vaccin4 = sum/num
    
    sum = 0
    num = 0
    for i in vaccin5:
        sum += i.price
        num += 1
    if num == 0:
        vaccin5 = 0
    else:
        vaccin5 = sum/num

    city = []
    for j in range(0,9):
        sum=0
        count=0
        vaccin = Vaccination.objects.filter(kind="종합백신", area=str(j))
        for i in vaccin :
            sum += i.price
            num += 1
        if num == 0:
            city.append(0)
        else:
            city.append(sum/num)
    cityname = ['종로, 중구, 용산','도봉, 강북, 성북, 노원','동대문, 중랑, 성동, 광진','강동, 송파','서초, 강남','동작, 관악, 금천','강서, 양천, 영등포, 구로','은평, 마포, 서대문']
    
    return render(request, 'main.html', {'corona':vaccin1, 'vaccin':vaccin2, 'cenel':vaccin3, 'sinjong':vaccin4, 'meddog':vaccin5, 'city':city, 'cityname':cityname})


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request, 'signup.html')