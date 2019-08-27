from django.shortcuts import render

# Create your views here.
def diary(request):
    return render(request, 'diary.html')