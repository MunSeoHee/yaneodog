from django.shortcuts import render, redirect
from django.core.paginator import Paginator

#table 로드
from .models import Health
from .models import Food
from .models import Record
from .models import Dog
from .models import Vaccination
from .models import Diagnosis
from .models import DailyLife

from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

# 강아지 정보 삭제 로직
def dogDelete(request, dog_id):
    #강아지 id 정보를 url로 받아온 뒤, 해당 id의 강아지를 삭제 후 diary페이지로 이동
    dog = Dog.objects.get(num=dog_id)
    dog.delete()
    return redirect('/diary')

#강아지 추가 로직
def dogAdd(request, dog_id):
    #새로운 강아지 객체(데이터)생성
    dog = Dog()
    #POST방식으로 넘어오는 데이터들을 각 필드에 삽입
    dog.num = request.POST['num']
    dog.gender = request.POST['gender']
    dog.birthday = request.POST['birthday']
    dog.name = request.POST['name']
    dog.kind = request.POST['kind']
    dog.image = request.FILES['image']
    #user 정보는 현재 로그인 중인 유저의 이름을 받아 저장
    dog.user = request.user.get_username()
    #새로운 데이터 저장 후 diary페이지로 이동
    dog.save()
    return redirect('/diary/'+str(request.POST['num']))

#특정 강아지의 다이어리 페이지
def diary_dog(request, dog_id):
    dog = Dog.objects.all().order_by('num')
    last_dog_num = dog.last().num + 1
    #로그인 중인 유저의 강아지만을 뽑아냄
    dog_infos = Dog.objects.filter(user=request.user.get_username())
    #선택한 강아지 id 값을 가지고 있는 데이터를 뽑아냄
    dog_info = dog_infos.get(num = dog_id)
    dog_num = dog_info.num

    #health 테이블에서 해당 강아지의 데이터 뽑아냄
    healths_list=Health.objects.filter(dog=dog_info)
    #5개씩 페이지 네이션
    paginator = Paginator(healths_list,5)
    page = request.GET.get('page2')
    healths = paginator.get_page(page)

    #food 테이블에서 해당 강아지 데이터 뽑아냄
    foods_list=Food.objects.filter(dog=dog_info)
    #5개씩 페이지 네이션
    paginator = Paginator(foods_list,5)
    page = request.GET.get('page1')
    foods = paginator.get_page(page)

    #record 테이블에서 해당 강아지 데이터 뽑아냄
    records_list=Record.objects.filter(dog=dog_info)
    #5개씩 페이지 네이션
    paginator = Paginator(records_list,5)
    page = request.GET.get('page3')
    records = paginator.get_page(page)

    #dailylife 테이블의 데이터들 중 해당 강아지 데이터를 날짜 순으로 정렬
    dailys = DailyLife.objects.filter(dog=dog_num).order_by('date')
    date = []
    weight = []
    walk = []
    morning_amount = []
    lunch_amount = []
    dinner_amount = []
    
    #정렬된 데이터를 차트에 넣기 위한 작업
    for i in dailys:
        #날짜 순으로 정렬된 몸무게를 배열에 삽입
        weight.append(i.weight)
        #날짜를 배열에 삽입
        df = DateFormat(i.date)
        k = df.format("Ymd")
        date.append(int(k))
        #날짜 순으로 정렬된 산책 정보를 배열에 삽입
        walk.append(i.walk)
        #날짜 순으로 정렬된 아침, 점심, 저녁 양을 배열에 삽입
        morning_amount.append(i.morning_amount)
        lunch_amount.append(i.lunch_amount)
        dinner_amount.append(i.dinner_amount)

    #diary페이지에 데이터들을 key:value 형식으로 보냄 
    return render(request, 'diary.html', {'walk':walk, 'morning_amount':morning_amount, 'lunch_amount':lunch_amount, 'dinner_amount':dinner_amount,
                                        'healths':healths, "foods":foods, "records":records, "dog_num":dog_num, "dog_info":dog_info, 'date':date, 
                                        'weight':weight, 'dog_infos':dog_infos, 'last_dog_num':last_dog_num})

#기본 다이어리 페이지
def diary(request):
    dog = Dog.objects.all().order_by('num')
    last_dog_num = dog.last().num + 1
    #로그인 중인 유저의 강아지 정보만을 추출
    dog_infos = Dog.objects.filter(user=request.user.get_username())
    #로그인 중인 유저의 강아지들 중 첫번째 강아지 정보를 뽑아냄
    dog_info = dog_infos[0]
    dog_num = dog_info.num

    #health, food, record 테이블에서 해당 강아지 정보를 뽑아내고 5개씩 페이지네이션
    healths_list=Health.objects.all()
    paginator = Paginator(healths_list,5)
    page = request.GET.get('page2')
    healths = paginator.get_page(page)

    foods_list=Food.objects.all()
    paginator = Paginator(foods_list,5)
    page = request.GET.get('page1')
    foods = paginator.get_page(page)

    records_list=Record.objects.all()
    paginator = Paginator(records_list,5)
    page = request.GET.get('page3')
    records = paginator.get_page(page)

    #dailylife테이블에서 해당 강아지 정보를 뽑아내고 날짜 순으로 정렬
    dailys = DailyLife.objects.filter(dog=dog_num).order_by('date')
    date = []
    weight = []
    walk = []
    morning_amount = []
    lunch_amount = []
    dinner_amount = []
    
    #차트에 넣기 위해 데이터를 배열에 넣는 작업
    for i in dailys:
        weight.append(i.weight)
        df = DateFormat(i.date)
        k = df.format("Ymd")
        date.append(int(k))
        walk.append(i.walk)
        morning_amount.append(i.morning_amount)
        lunch_amount.append(i.lunch_amount)
        dinner_amount.append(i.dinner_amount)

    #diary 페이지에 데이터를 key:value 값으로 보냄
    return render(request, 'diary.html', {'walk':walk, 'morning_amount':morning_amount, 'lunch_amount':lunch_amount, 'dinner_amount':dinner_amount,
                                        'healths':healths, "foods":foods, "records":records, "dog_num":dog_num, "dog_info":dog_info, 'date':date, 
                                        'weight':weight, 'dog_infos':dog_infos, 'last_dog_num':last_dog_num})


#예방접종 페이지 로직
def vaccination(request, dog_id):
    #url로 받아온 해당 강아지 id를 통해 dog테이블에서 해당 강아지 객체(데이터)를 받아옴
    dog_info = Dog.objects.get(num = dog_id)
    dog_pk = dog_id
    dog_infos = Dog.objects.filter(user=request.user.get_username())
    #vaccination 테이블에서 해당 강아지의 데이터를 뽑아냄
    vaccins = Vaccination.objects.filter(dog=dog_pk)

    #예방접종 기록 페이지에 key:value 형식으로 값 보냄
    return render(request, 'diary_vaccination.html', {"vaccins":vaccins, "dog_num":dog_pk, "dog_infos":dog_infos})

#예방접종 기록 추가 로직
def vaccinAdd(request):
    #hidden 필드로 넘어온 강아지 객체 값
    dog_pk = request.GET['dog']
    
    #vaccination 테이블에 새로운 객체(데이터)추가
    vaccin = Vaccination()
    #GET 형식으로 넘어온 데이터들을 해당 필드에 삽입
    vaccin.price = request.GET['price']
    vaccin.hospital = request.GET['hospital']
    vaccin.date = request.GET['date']
    vaccin.count = request.GET['count']
    vaccin.record = request.GET['record']
    vaccin.kind = request.GET['kind']
    vaccin.area = request.GET['area']
    dog = Dog.objects.get(pk=dog_pk)
    vaccin.dog = dog
    #새로 추가된 데이터 저장 후, 예방접종 기록 페이지로 이동
    vaccin.save()

    return redirect('/diary/vaccination/'+dog_pk)

#예방접종 기록 삭제 로직
def vaccinDelete(request, vaccin_id, dog_id):
    #url로 삭제할 vaccination 테이블의 데이터 번호를 받아와서, 해당 데이터 삭제 후 예방접종 기록 페이지로 이동
    vaccin = Vaccination.objects.get(id=vaccin_id)
    vaccin.delete()
    return redirect('/diary/vaccination/'+str(dog_id))

#일상기록 페이지 로직
def dailylife(request, dog_id):
    #url로 정보를 확인할 강아지 번호를 받아와서 해당 강아지의 정보를 dialylife테이블에서 뽑아냄
    dog_info = Dog.objects.get(num=dog_id)
    dog_pk = dog_info.num
    dog_infos = Dog.objects.filter(user=request.user.get_username())
    dailys = DailyLife.objects.filter(dog=dog_pk)
    #일상기록 페이지에 key:value 형식으로 데이터 보내면서 이동
    return render(request, 'diary_dailylife.html', {"dailys":dailys, "dog_num":dog_pk, "dog_infos":dog_infos})

#일상 추가 로직
def dailyAdd(request):
    #dailylife 테이블에 새로운 객체(데이터)생성 후 GET방식으로 넘어오는 데이터들을 각 필드에 삽입
    dog_pk = request.GET['dog']

    daily = DailyLife()
    daily.date = request.GET['date']
    if request.GET['walk'] == '':
        daily.walk = None
    else:
        daily.walk = request.GET['walk']
    daily.weight = request.GET['weight']
    daily.dung = request.GET['dung']
    daily.Pee = request.GET['Pee']
    daily.morning = request.GET['morning']
    daily.morning_amount = request.GET['morning_amount']
    daily.lunch = request.GET['lunch']
    daily.lunch_amount = request.GET['lunch_amount']
    daily.dinner = request.GET['dinner']
    daily.dinner_amount = request.GET['dinner_amount']
    daily.shower = request.GET['shower']
    daily.medicine = request.GET['medicine']
    daily.puke = request.GET['puke']
    daily.behavior = request.GET['behavior']
    daily.record = request.GET['record']
    
    dog = Dog.objects.get(pk=dog_pk)
    daily.dog = dog
    daily.save()
    #데이터 저장 후 일상 페이지로 이동
    return redirect('/diary/dailylife/'+dog_pk)

#일상 삭제 로직
def dailyDelete(request, daily_id, dog_id):
    #url로 삭제할 데이터 id를 받아온 뒤 해당 id를 가진 데이터 삭제
    daily = DailyLife.objects.get(id=daily_id)
    daily.delete()
    #일상 페이지로 이동
    return redirect('/diary/dailylife/'+str(dog_id))

#음식 정보 추가 로직
def foodAdd(request):
    dog_pk = request.GET['dog']
    #food테이블에 새 객체(데이터)생성 후 get 방식으로 넘어오는 데이터를 해당 필드에 삽입
    food = Food()
    food.food = request.GET['food']
    dog = Dog.objects.get(pk=dog_pk)
    food.dog = dog
    food.save()
    #저장 후 다이어리 페이지로 이동
    return redirect('/diary/'+dog_pk)

#음식 정보 삭제 로직
def foodDelete(request, food_id, dog_id):
    #삭제 할 데이터의 id 값을 url로 받아와서 food 테이블에서 해당 데이터 삭제
    food = Food.objects.get(id=food_id)
    food.delete()
    #삭제 후 다이어리 페이지로 이동
    return redirect('/diary/'+str(dog_id))

#건강 정보 추가 로직
def healthAdd(request):
    dog_pk = request.GET['dog']
    #health테이블에 새 객체(데이터)생성 후 get 방식으로 넘어오는 데이터를 해당 필드에 삽입
    health = Health()
    health.health = request.GET['health']
    dog = Dog.objects.get(pk=dog_pk)
    health.dog = dog
    health.save()
    #저장 후 다이어리 페이지로 이동
    return redirect('/diary/'+dog_pk)

#건강 정보 삭제 로직
def healthDelete(request, health_id, dog_id):
    #삭제 할 데이터의 id 값을 url로 받아와서 health 테이블에서 해당 데이터 삭제
    health = Health.objects.get(id=health_id)
    health.delete()
    #삭제 후 다이어리 페이지로 이동
    return redirect('/diary/'+str(dog_id))

#기타 기록 추가 로직
def recordAdd(request):
    dog_pk = request.GET['dog']
    #record테이블에 새 객체(데이터)생성 후 get 방식으로 넘어오는 데이터를 해당 필드에 삽입
    record = Record()
    record.record = request.GET['record']
    dog = Dog.objects.get(pk=dog_pk)
    record.dog = dog
    record.save()
    #저장 후 다이어리 페이지로 이동
    return redirect('/diary/'+dog_pk)

#기타 기록 삭제 로직
def recordDelete(request, record_id, dog_id):
    #삭제 할 데이터의 id 값을 url로 받아와서 record 테이블에서 해당 데이터 삭제
    record = Record.objects.get(id=record_id)
    record.delete()
    #삭제 후 다이어리 페이지로 이동
    return redirect('/diary/'+str(dog_id))

#진단정보 페이지 로직
def diagnosis(request, dog_id):
    #선택된 강아지의 정보를 뽑아내어서 key:value 형식으로 데이터 진단 정보 페이지에 데이터 전송
    dog_info = Dog.objects.get(num=dog_id)
    dog_pk = dog_info.num
    dog_infos = Dog.objects.filter(user=request.user.get_username())
    diagnosis = Diagnosis.objects.filter(dog=dog_pk)
    return render(request, 'diary_diagnosis.html', {"diagnosis":diagnosis, "dog_num":dog_pk, "dog_infos":dog_infos})

#진단 정보 삭제 로직
def diagDelete(request, diag_id, dog_id):
    #삭제 할 데이터의 id 값을 url로 받아와서 diagnosis 테이블에서 해당 데이터 삭제
    diag = Diagnosis.objects.get(id=diag_id)
    diag.delete()
    #삭제 후 진단 정보 페이지로 이동
    return redirect('/diary/diagnosis/'+str(dog_id))

#진단 정보 추가 로직
def diagAdd(request):
    dog_pk = request.GET['dog']
    #diagnosis테이블에 새 객체(데이터)생성 후 get 방식으로 넘어오는 데이터를 해당 필드에 삽입
    diag = Diagnosis()
    diag.kind = request.GET['kind']
    diag.date = request.GET['date']
    diag.area = request.GET['area']
    diag.hospital = request.GET['hospital']
    diag.medicine = request.GET['medicine']
    diag.next_date = request.GET['next_date']
    diag.price = request.GET['price']
    diag.record = request.GET['record']
    dog = Dog.objects.get(pk=dog_pk)
    diag.dog = dog
    diag.save()
    #추가 후 진단 정보 페이지로 이동
    return redirect('/diary/diagnosis/'+dog_pk)