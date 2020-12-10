from django.contrib import admin
# Register your models here.
from .models import Dog
from .models import Vaccination
from .models import Diagnosis
from .models import DailyLife
from .models import Health
from .models import Food
from .models import Record

# Register your models here.
admin.site.register(Dog)
admin.site.register(Vaccination)
admin.site.register(Diagnosis)
admin.site.register(DailyLife)
admin.site.register(Health)
admin.site.register(Food)
admin.site.register(Record)