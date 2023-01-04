from django.shortcuts import render

# Create your views here.
def DataTest(request):
    return render(request, 'api/home.html')
