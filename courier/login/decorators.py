
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group


def unauthenticated_users(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('success')
        else:
            # return redirect('success')
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # print('Working',allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print('Working',group)
            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page',group)

        return wrapper_func
    return decorator



def allowed_post(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            post = request.user.userprofile.post
            # print('Working', post)
            if post in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page', post)
        return wrapper_func
    return decorator


# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             print('Working',allowed_roles)
#             group = request.user.groups
#             username = request.user.groups.exists()
#             print (group)
#             print (username)
#
#             # Action if not existing
#             # if request.user.groups.exists():
#             # group = request.user.groups.all()[0].name
#             # print('Working',group)
#             # if group in allowed_roles:
#             return view_func(request,*args, **kwargs)
#             # else:
#             # return HttpResponse('You are not authorized to view this page',group)
#
#         return wrapper_func
#     return decorator



def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Staff':
            # return HttpResponse('You are not authorized to view this page')
            return redirect('index')

        if group == 'Admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function