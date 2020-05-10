from django.urls import path
from . import views

urlpatterns = [
path('courier_form/', views.courier_form, name='courier_form'),
path('courier_detail/', views.courier_detail, name='courier_detail'),

]