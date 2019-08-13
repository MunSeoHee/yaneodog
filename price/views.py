from django.shortcuts import render

# Create your views here.
def pricemap(request):
    return render(request, 'pricemap.html')