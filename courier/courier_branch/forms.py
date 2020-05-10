from django.forms import ModelForm

from .models import CourierDetails
from django import forms

class CourierForm(forms.ModelForm):
    class Meta:
        model = CourierDetails
        fields = '__all__'