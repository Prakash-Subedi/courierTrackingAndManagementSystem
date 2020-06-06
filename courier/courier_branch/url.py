from django.urls import path
from . import views, branch_view

urlpatterns = [
path('courier_form/', views.courier_form, name='courier_form'),
path('courier_detail/', views.courier_detail, name='courier_detail'),
path('tracked_courier/', views.courier_tracking, name='tracked_courier'),
path('edit_courier/<int:pk>', views.edit_courier, name='edit_courier'),
path('courier_search/', views.courier_search, name='courier_search'),
path('search_data/', views.search_data, name='search_data'),
path('courier_detail_branch/', views.courier_detail_branch, name='courier_detail_branch'),
path('branches/', branch_view.branch, name='branches'),
path('del_courier/<int:pk>', views.del_courier, name='del_courier'),

]