from django.contrib import admin

from.models import CourierDetails
from .models import Branch
from .models import Comments
from .models import DayBook

#  Register your models here.

admin.site.register(CourierDetails)
admin.site.register(Branch)
admin.site.register(Comments)
admin.site.register(DayBook)