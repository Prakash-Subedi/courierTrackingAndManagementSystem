from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [

    #path('login/', views.login, name='login'),


    path('login/', LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('logout/', views.user_logout, name='logout'),
    path('notice/', views.notice, name='notice'),
    path('notice_form/', views.notice_form, name='notice_form'),
    path('notice_detail/<int:pk>', views.notic_detail, name='notice_detail'),



     # path(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'})
]