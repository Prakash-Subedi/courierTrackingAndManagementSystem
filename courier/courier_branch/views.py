from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import CourierForm
from .models import CourierDetails
from django.http import Http404
from django.shortcuts import get_object_or_404


# Create your views here.

# from ..login.models import UserProfile

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
    courier_pending = CourierDetails.objects.filter(courier_status='Pending')
    courier_delivered = CourierDetails.objects.filter(courier_status='Delivered')
    pending = CourierDetails.objects.filter(courier_status='Pending').count()
    delivered = CourierDetails.objects.filter(courier_status='Delivered').count()
    # { % url
    # 'edit_courier'
    # courier.courier_id %}

    return render(request, 'courier/courierdetail.html', {'courier_delivered': courier_delivered,'courier_pending': courier_pending,'courier_info': courier_info, 'pending': pending, 'delivered': delivered})



def courier_tracking(request):

    tracking_id = request.GET.get('courier_id')
    # print(tracking_id)

    if tracking_id:
        try:
            courier_details = CourierDetails.objects.get(courier_tracking_id=tracking_id)
            return render(request, 'courier/tracked_courier.html', {'courier_details': courier_details})
        except ObjectDoesNotExist:
            raise Http404('Courier with this Tracking ID is not found. Check Tracking ID, Thank you !!')
    else:
        return redirect('success')

def edit_courier (request, pk ):
    courier = get_object_or_404(CourierDetails, courier_id=pk)
    if request.method == "POST":
        form= CourierForm(request.POST, instance=courier)
        if form.is_valid():
            form.save()
            return redirect('courier_detail')
    else:
        form = CourierForm(instance=courier)
    return render(request, 'courier/edit_courier.html', {'form': form})






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