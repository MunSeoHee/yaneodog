from django.shortcuts import render
from django.shortcuts import HttpResponse, render_to_response
from diary.models import Vaccination
import random, json
# Create your views here.

def compare(request):
    vaccin1 = Vaccination.objects.filter(kind="코로나 장염")
    vaccin2 = Vaccination.objects.filter(kind="종합백신")
    vaccin3 = Vaccination.objects.filter(kind="켄넬 코프")
    vaccin4 = Vaccination.objects.filter(kind="신종플루")
    vaccin5 = Vaccination.objects.filter(kind="광견병")
    seoul = []
    sum = 0
    num = 0
    for i in vaccin1:
        sum += i.price
        num += 1
    if num == 0:
        seoul.append(0)
    else:
        seoul.append(sum/num)
        
    sum = 0
    num = 0
    for i in vaccin2:
        sum += i.price
        num += 1
    if num == 0:
        seoul.append(0)
    else:
        seoul.append(sum/num)

    sum = 0
    num = 0
    for i in vaccin3:
        sum += i.price
        num += 1
    if num == 0:
        seoul.append(0)
    else:
        seoul.append(sum/num)
    

    sum = 0
    num = 0
    for i in vaccin4:
        sum += i.price
        num += 1
    if num == 0:
        seoul.append(0)
    else:
        seoul.append(sum/num)
    
    sum = 0
    num = 0
    for i in vaccin5:
        sum += i.price
        num += 1
    if num == 0:
        seoul.append(0)
    else:
        seoul.append(sum/num)



    city = request.GET.get('city')
    print(type(city))
    if city == '1':
        cityname = "종로, 중구, 용산"
    elif city == '2':
        cityname = "도봉, 강북, 성북, 노원"
    elif city == '3':
        cityname = "동대문, 중랑, 성동, 광진"
    elif city == '4':
        cityname = "강동, 송파"
    elif city == '5':
        cityname = "서초, 강남"
    elif city == '6':
        cityname = "동작, 관악, 금천"
    elif city == '7':
        cityname = "강서, 양천, 영등포, 구로"
    elif city == '8':
        cityname = "은평, 마포, 서대문"
    else:
        cityname="서울"
    print(cityname)

    if city != '0' and city != None:
        city_price = []
        vaccin1 = Vaccination.objects.filter(kind="코로나 장염", area=str(city))
        vaccin2 = Vaccination.objects.filter(kind="종합백신", area=str(city))
        vaccin3 = Vaccination.objects.filter(kind="켄넬 코프", area=str(city))
        vaccin4 = Vaccination.objects.filter(kind="신종플루", area=str(city))
        vaccin5 = Vaccination.objects.filter(kind="광견병", area=str(city))
        sum = 0
        num = 0
        for i in vaccin1:
            sum += i.price
            num += 1
        if num == 0:
            city_price.append(0)
        else:
            city_price.append(sum/num)
            
        sum = 0
        num = 0
        for i in vaccin2:
            sum += i.price
            num += 1
        if num == 0:
            city_price.append(0)
        else:
            city_price.append(sum/num)

        sum = 0
        num = 0
        for i in vaccin3:
            sum += i.price
            num += 1
        if num == 0:
            city_price.append(0)
        else:
            city_price.append(sum/num)
        

        sum = 0
        num = 0
        for i in vaccin4:
            sum += i.price
            num += 1
        if num == 0:
            city_price.append(0)
        else:
            city_price.append(sum/num)
        
        sum = 0
        num = 0
        for i in vaccin5:
            sum += i.price
            num += 1
        if num == 0:
            city_price.append(0)
        else:
            city_price.append(sum/num)
    else:
        city = '서울'
        city_price = [0]
    
    

    return render(request, 'compare.html', {'seoul':seoul, 'city_price':city_price, 'city':city, 'cityname':cityname})

    


def main_page(request):

    return render_to_response('main_page.html')

