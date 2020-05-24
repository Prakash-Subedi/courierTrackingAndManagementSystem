from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import CourierForm
from .models import CourierDetails, Branch
from django.http import Http404
from django.shortcuts import get_object_or_404
from .decorators import allowed_post
import datetime


# Create your views here.

# from ..login.models import UserProfile
@login_required(login_url="/login/")
@allowed_post(allowed_roles=['Admin', 'Manager', 'staff'])
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

# @login_required(login_url="/login/")
# def courier_detail(request):
#     branchs= request.user.userprofile.branch
#     try:
#         iD = Branch.objects.get(branch_name=branchs)
#         branch_iD = iD.id
#     except ObjectDoesNotExist:
#         raise Http404('Branch not found !!')
#     posts = request.user.userprofile.post
#     if posts == 'Staff':
#         courier_send_pen = CourierDetails.objects.filter(sending_branch_name= branch_iD,  courier_status='Pending')
#         courier_rec_pen = CourierDetails.objects.filter(receiving_branch=branch_iD,  courier_status='Pending')
#         return render(request, 'courier/courierdetail.html', { })
#     else:
#         courier_info = CourierDetails.objects.all()
#         courier_pending = CourierDetails.objects.filter(courier_status='Pending')
#         courier_delivered = CourierDetails.objects.filter(courier_status='Delivered')
#         pending = CourierDetails.objects.filter(courier_status='Pending').count()
#         delivered = CourierDetails.objects.filter(courier_status='Delivered').count()

@login_required(login_url="/login/")
@allowed_post(allowed_roles=['Admin', 'Manager'])
def courier_detail(request):
    branchs = request.user.userprofile.branch
    try:
        iD = Branch.objects.get(branch_name=branchs)
        branch_iD = iD.id
    except ObjectDoesNotExist:
        raise Http404('Branch not found !!')

    posts = request.user.userprofile.post
    print(posts)

    courier_info = CourierDetails.objects.all()
    courier_pending = CourierDetails.objects.filter(courier_status='Pending')
    courier_delivered = CourierDetails.objects.filter(courier_status='Delivered')
    pending = CourierDetails.objects.filter(courier_status='Pending').count()
    delivered = CourierDetails.objects.filter(courier_status='Delivered').count()
    # { % url
    # 'edit_courier'
    # courier.courier_id %}

    return render(request, 'courier/courierdetail.html', {'courier_delivered': courier_delivered,'courier_pending': courier_pending,'courier_info': courier_info, 'pending': pending, 'delivered': delivered})


@login_required(login_url="/login/")
def courier_detail_branch(request):
    branchs = request.user.userprofile.branch
    try:
        iD = Branch.objects.get(branch_name=branchs)
        branch_iD = iD.id
    except ObjectDoesNotExist:
        raise Http404('Branch not found !!')
    courier_info = CourierDetails.objects.all()
    courier_pending_rec = CourierDetails.objects.filter(receiving_branch=branch_iD,courier_status='Pending')
    courier_pending_sen = CourierDetails.objects.filter(sending_branch_name=branch_iD, courier_status='Pending')
    pending = CourierDetails.objects.filter(courier_status='Pending').count()
    delivered = CourierDetails.objects.filter(courier_status='Delivered').count()
    # { % url
    # 'edit_courier'
    # courier.courier_id %}

    return render(request, 'courier/courierdetails_branch.html', {'courier_pending_sen': courier_pending_sen,'courier_pending_rec': courier_pending_rec, 'pending': pending, 'delivered': delivered})



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
@login_required(login_url="/login/")
def edit_courier(request, pk):
    courier = get_object_or_404(CourierDetails, courier_id=pk)
    if request.method == "POST":
        form= CourierForm(request.POST, instance=courier)
        if form.is_valid():
            form.save()

            return redirect('courier_detail_branch')
    else:
        form = CourierForm(instance=courier)
    return render(request, 'courier/edit_courier.html', {'form': form})

@login_required(login_url="/login/")
def courier_search(request):
    branches = Branch.objects.all()
    post = request.user.userprofile.post
    print (post)

    if post == 'Staff':
        return render(request, 'courier/courier_search_staff.html')
    else:
        return render(request, 'courier/courier_search.html', {'branches': branches})





def search_data(request):

    branch_type = request.GET.get('Branch_type')
    print(branch_type)
    if (request.user.userprofile.post) == 'Staff':
        branch_name = request.user.userprofile.branch
        try:
            iD= Branch.objects.get(branch_name=branch_name)
            branch_iD=iD.id
        except ObjectDoesNotExist:
            raise Http404('Branch not found !!')
    else:
        branch_name = request.GET.get('Branch')
        try:
            iD= Branch.objects.get(branch_name=branch_name)
            branch_iD=iD.id
        except ObjectDoesNotExist:
            raise Http404('Branch not found !!')

    courier_status = request.GET.get('Status')
    try:
        date_from = datetime.datetime.strptime(request.GET['date_from'], '%Y-%m-%d')
        date_to = datetime.datetime.strptime(request.GET['date_to'], '%Y-%m-%d')
    except ValueError:
        raise Http404('Please select correct date')
    try:
        if branch_type == 'Receiving':
            courier_details = CourierDetails.objects.filter(receiving_branch= branch_iD,  courier_status=courier_status, received_at__range=(date_from, date_to))
        else:
            courier_details = CourierDetails.objects.filter(sending_branch_name= branch_iD,  courier_status=courier_status, received_at__range=(date_from, date_to))

    except ObjectDoesNotExist:
        raise Http404('Courier with this Tracking ID is not found. Check Tracking ID, Thank you !!')

    return render(request, 'courier/search_data.html',{'courier_details':courier_details, 'branch_type':branch_type,'branch_name':branch_name, 'courier_status':courier_status, 'date_from':date_from, 'date_to': date_to })




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