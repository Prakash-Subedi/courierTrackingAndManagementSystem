from django.urls import path
from . import views

urlpatterns = [
path('courier_form/', views.courier_form, name='courier_form'),
path('courier_detail/', views.courier_detail, name='courier_detail'),
path('tracked_courier/', views.courier_tracking, name='tracked_courier'),
path('edit_courier/<int:pk>', views.edit_courier, name='edit_courier')
]