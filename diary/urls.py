from django.urls import path
from . import views

urlpatterns = [
    #path('url 형식', views파일.실행할 함수(로직), 별칭)
    #해당 url 형식으로 요청이 들어오면 views파일의 해당 함수를 실행하고 이것의 이름을 별칭으로 지음
    path('', views.diary, name='diary'),
    path('dogDelete/<int:dog_id>', views.dogDelete, name='dog_delete'),
    path('dogAdd/<int:dog_id>', views.dogAdd, name='dog_add'),
    path('/<int:dog_id>', views.diary_dog, name='diary_dog'),
    path('/vaccination/<int:dog_id>', views.vaccination, name='vaccination'),
    path('/diagnosis/<int:dog_id>', views.diagnosis, name="diagnosis"),
    path('/dailylife/<int:dog_id>', views.dailylife, name="dailylife"),
    path('/foodAdd', views.foodAdd, name="food_add"),
    path('/dailyAdd', views.dailyAdd, name="daily_add"),
    path('/healthAdd', views.healthAdd, name="health_add"),
    path('/recordAdd', views.recordAdd, name="record_add"),
    path('/vaccinAdd', views.vaccinAdd, name="vaccin_add"),
    path('/diagAdd', views.diagAdd, name="diag_add"),
    path('/diagDelete/<int:diag_id>/<int:dog_id>', views.diagDelete, name='diag_delete'),
    path('/dailyDelete/<int:daily_id>/<int:dog_id>', views.dailyDelete, name='daily_delete'),
    path('/foodDelete/<int:food_id>/<int:dog_id>', views.foodDelete, name='food_delete'),
    path('/healthDelete/<int:health_id>/<int:dog_id>', views.healthDelete, name='health_delete'),
    path('/recordDelete/<int:record_id>/<int:dog_id>', views.recordDelete, name='record_delete'),
    path('/vaccinDelete/<int:vaccin_id>/<int:dog_id>', views.vaccinDelete, name='vaccin_delete'),
]
