from django.db import models
from django.contrib.auth.models import User

#강아지 table
class Dog(models.Model):
    #user와 연결되는 필드
    user = models.CharField(max_length=200, null=True)

    #기본 키 
    num = models.IntegerField(primary_key=True)

    #강아지 기본 정보 (성별, 생일, 이름, 종류)
    gender = models.BooleanField()
    birthday = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)

    #강아지 이미지 저장, 값이 없을 경우 기본 값 지정
    image = models.ImageField(upload_to='images/', null=True, default = "{% static 'main_img01.jpg' %}")

#음식 table
class Food(models.Model):
    #강아지 음식 특이사항 기록 필드
    food = models.CharField(max_length=200, blank=True)
    #강아지 정보 외래키
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)  #동물 id

#건강 정보 table
class Health(models.Model):
    #강아지 건강 특이사항 기록 필드
    health = models.CharField(max_length=200, blank=True)
    #강아지 정보 외래키
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)  #동물 id

#기록 정보 table
class Record(models.Model):
    #강아지 기타 특이사항 기록 필드
    record = models.CharField(max_length=200, blank=True)
    #강아지 정보 외래키
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)  #동물 id
    

#백신 기록 table
class Vaccination(models.Model):
    kind = models.CharField(max_length=200)         #백신 종류
    count = models.CharField(max_length=200, blank=True)#몇차?   
    date = models.DateTimeField('date published', null=True)   #날짜
    area = models.CharField(max_length=200)         #지역
    hospital = models.CharField(max_length=200)     #병원이름
    price = models.IntegerField(null=True)                   #가격
    record = models.TextField(blank=True)           #기타 기록

    #강아지 정보 외래키
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)  #동물 id

#진료 기록 table
class Diagnosis(models.Model):
    kind = models.CharField(max_length=200)         #진료
    date = models.DateTimeField('date published', null=True)   #날짜
    area = models.CharField(max_length=200)         #지역
    hospital = models.CharField(max_length=200)     #병원이름
    medicine = models.CharField(max_length=200, blank=True)     #약
    next_date = models.DateTimeField('date published', null=True)   #다음 진료일
    price = models.IntegerField(null=True)                   #가격
    record = models.TextField(blank=True)           #기타 기록

    #강아지 정보 외래키
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)  #동물 id

#일상 기록 table
class DailyLife(models.Model):
    date = models.DateTimeField('date published')   #날짜
    walk = models.IntegerField(null=True)    #산책
    weight = models.IntegerField(null=True)  #몸무게
    dung = models.CharField(max_length=200, blank=True) #똥 상태
    Pee = models.CharField(max_length=200, blank=True)  #소변 상태
    morning = models.NullBooleanField(blank=True)  #아침 급여 여부
    morning_amount = models.IntegerField(blank=True, null=True)    #아침 급여 양
    lunch = models.NullBooleanField(null=True)  #점심 급여 여부
    lunch_amount = models.IntegerField(blank=True, null=True)    #점심 급여 양
    dinner = models.NullBooleanField(null=True)  #저녁 급여 여부
    dinner_amount = models.IntegerField(blank=True, null=True)    #저녁 급여 양
    shower = models.NullBooleanField(null=True)  #목욕
    medicine = models.CharField(max_length=200, blank=True) #약
    puke = models.CharField(max_length=200, blank=True) #구토
    behavior = models.CharField(max_length=200, blank=True) #이상행동
    record = models.TextField(blank=True)           #기타 기록

    #강아지 정보 외래키
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)  #동물 id
