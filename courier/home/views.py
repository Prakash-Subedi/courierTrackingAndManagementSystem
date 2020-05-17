from django.shortcuts import render
from django.http import HttpResponse
from .decorators import unauthenticated_user

# Create your views here.



def home(request):
    return render(request, 'home.html', {'name': 'manisha'})


@unauthenticated_user
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request, 'about.html')