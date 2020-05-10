from django.shortcuts import render, redirect
from .forms import CourierForm

# Create your views here.
from .models import CourierDetails



def courier_form(request):
        form = CourierForm()
        if request.method == 'POST':
            form = CourierForm(request.POST)
            if form.is_valid():
                form.save()
                courier_nam = form.cleaned_data.get('courier_name')
                courier_info = CourierDetails.objects.get(courier_name=courier_nam)
                return render(request, 'courier/courier_just_recorded.html', {'courier_info': courier_info})
                # return redirect('success')
            else:
                return render(request, 'courier/record.html', {'form': form})

        else:
            return render(request, 'courier/record.html', {'form': form})

def courier_detail(request):
    courier_info = CourierDetails.objects.all()
    return render(request, 'courier/courierdetail.html',{'courier_info': courier_info})

    # def courier_form(request):
    #     form = CourierForm()
    #     if request.method == 'POST':
    #         form = CourierForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             courier_name = form.cleaned_data.get('courier_id')
    #             print(courier_name)
    #             return redirect('success')
    #         else:
    #             return render(request, 'courier/record.html', {'form': form})
    #
    #     else:
    #         return render(request, 'courier/record.html', {'form': form})