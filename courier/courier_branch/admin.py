from django.contrib import admin

from.models import CourierDetails
from .models import Branch
from .models import Comments

#  Register your models here.

admin.site.register(CourierDetails)
admin.site.register(Branch)
admin.site.register(Comments)