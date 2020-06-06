from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from .decorators import unauthenticated_user
from django.core.mail import send_mail

# Create your views here.
from .forms import ContactForm


def home(request):
    return render(request, 'home.html', {'name': 'manisha'})


@unauthenticated_user
def index(request):
    return render(request, 'index.html')

def contact(request):
    forms = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            subject = 'Thank you for contracting us'
            body = 'we will get to you very soon'
            from_email = settings.EMAIL_HOST_USER
            to_do = [email]
            send_mail(subject, body, from_email, to_do, fail_silently=True )



            # contact_info = ContactForm.objects.get(full_name=name)

            return render(request, 'contact.html', {'form': forms, 'message': 'Thank you for contracting us' })
            # return redirect('success')
        else:
            return render(request, 'contact.html', {'form': form, 'message': 'Somthing went wrong, please fill the form correctly'})
    else:
        return render(request, 'contact.html', {'form': forms })

def about(request):
    return render(request, 'about.html')

def calculate(request):
    try:
        hight = float(request.GET.get('hight'))
        hight_unit = request.GET.get('hight_unit')
        if hight_unit == 'cm':
            hight /= 100
            hight_unit='m'
        width = float(request.GET.get('width'))
        width_unit = request.GET.get('width_unit')
        if width_unit == 'cm':
            width /= 100
            width_unit ='m'
        length = float(request.GET.get('width'))
        length_unit = request.GET.get('length_unit')
        if length_unit == 'cm':
            length /= 100
            length_unit= 'm'
        wight = float(request.GET.get('wight'))
        wight_unit = request.GET.get('wight_unit')
        if wight_unit == 'G':
            wight /= 1000
            wight_unit='kg'

        type = request.GET.get('type')

        if type == 'National':
            if wight<= 2 :
                rate = 200
                cost = (length*hight*width) *rate
            else:
                rate = 200
                cost = (length*hight*width)*rate+(wight-2)*50
            if cost <= 50:
                cost=50
        else:
            if wight <= 2:
                rate = 400
                cost = (length * hight * width) * rate
            else:
                rate = 400
                cost = (length * hight * width) * rate + (wight - 2) * 50
            if cost <= 200:
                cost = 200
        return render(request, 'cal_result.html', {'cost':cost, 'length':length, 'width':width, 'hight':hight, 'wight':wight,'length_unit':length_unit,'width_unit':width_unit,'hight_unit':hight_unit, 'wight_unit':wight_unit, 'type':type })

    except TypeError or ValueError:
        raise Http404('Your input data is not correct, please enter data correctly !!')