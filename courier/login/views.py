from django.contrib.auth import logout
from django.http import HttpResponseRedirect, response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_users, allowed_users, admin_only, allowed_post
from .forms import RegisterForm, UserProfileForm, NoticeForm
import datetime
from .models import Notice
from django.urls import reverse

# Create your views here.
# @unauthenticated_users
# def login(request):
#     return render(request, 'login.html')



@login_required(login_url="/login/")
@allowed_post(allowed_roles=['Admin', 'Manager'])
def register(request):
    form = RegisterForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            group = Group.objects.get(name='Staff')
            user.groups.add(group)
            return redirect('success')
        else:
            return render(request, 'registration/register.html', {'form': form, 'profile_form': profile_form})

    else:
        return render(request, 'registration/register.html', {'form': form, 'profile_form': profile_form})




@login_required(login_url="/login/")
# @allowed_users(allowed_roles=['Admin']) # add allowed list
# @admin_only
def success(request):
    note = Notice.objects.all().order_by('-date')[:3]
    return render(request, 'success/success.html',{'note': note})

@login_required(login_url="/login/")
def notice(request):
    note = Notice.objects.filter(date__range=(datetime.datetime.today()-datetime.timedelta(days=30), datetime.datetime.today())).order_by('-date')
    return render(request, 'notice.html',{'note': note})

@login_required(login_url="/login/")
def notic_detail(request, pk):
    notice = get_object_or_404(Notice, id=pk)
    if request.method == 'POST':
        notice.delete()
        return redirect('notice')
    return render(request, 'notice_details.html', {'notice': notice})

@login_required(login_url="/login/")
@allowed_post(allowed_roles=['Admin'])
def notice_form(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notice')
        else:
            return render(request, 'notice_form.html', {'form': form})

    else:
        form = NoticeForm()
        return render(request, 'notice_form.html', {'form': form})

# @unauthenticated_users
def user_logout(request):
    # if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('index'),)




    # from django import template
    # from django.contrib.auth.models import Group
    #
    # register = template.Library()
    #
    # @register.filter(name='has_group')
    # def has_group(user, group_name):
    #     group = Group.objects.get(name=group_name)
    #     return group in user.groups.all()

    # def register(request):
    #     form = RegisterForm()
    #     if request.method == 'POST':
    #         form = RegisterForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('success')
    #         else:
    #             return render(request, 'registration/register.html', {'form': form})
    #
    #     else:
    #         return render(request, 'registration/register.html', {'form': form})

    #after crispy form
    # def register(request):
    #     form = RegisterForm()
    #     if request.method == 'POST':
    #         form = RegisterForm(request.POST)
    #
    #         if form.is_valid():
    #             user = form.save()
    #             group = Group.objects.get(name='Staff')
    #             user.groups.add(group)
    #             return redirect('success')
    #         else:
    #             return render(request, 'registration/register.html', {'form': form})
    #
    #     else:
    #         return render(request, 'registration/register.html', {'form': form})
