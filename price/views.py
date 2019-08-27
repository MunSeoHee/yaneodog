from django.shortcuts import render

# Create your views here.
def pricemap(request):
    return render(request, 'pricemap.html')

def compare(request):
    return render(request, 'compare.html')

    


