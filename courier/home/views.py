from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'manisha'})


def index(request):
    return render(request, 'index.html', {'name': 'manisha'})