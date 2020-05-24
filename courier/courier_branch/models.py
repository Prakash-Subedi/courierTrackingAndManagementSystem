from django.db import models
from django.db.models import DateTimeField
from hashid_field import HashidAutoField    # pip install django-hashid-field
from phone_field import PhoneField   # pip install django-phone-field
from django.utils import timezone

# Create your models here.



# branch.

class Branch(models.Model):
    branch_name = models.CharField(max_length=30, blank=False, unique=True)
    branch_address = models.CharField(max_length=50, blank=False)
    branch_phone_no = models.CharField(blank=True, max_length=16, help_text='Contact phone number')
    branch_des = models.TextField()
    branch_pic = models.ImageField(upload_to='branch/', blank=True)  # python -m pip install Pillow
    branch_created_at = models.DateTimeField(auto_now_add=True,)
    branch_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_name

    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = timezone.now()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(DateTimeField, self).pre_save(model_instance, add)

# Branch_CHOICE = ( Branch.objects.only('branch_name'))

# courier main class



class Courier(models.Model):
    courier_id = models.AutoField(primary_key=True)  # auto generated
    courier_name = models.CharField(max_length=100,blank=False, unique=True, help_text='Enter unique name of courier')
    courier_description = models.TextField(max_length=300, blank=True, help_text='Notes about Courier')
    sending_branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, help_text='This Branch')

# courier base class for more details

class CourierDetails(Courier):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Delivered", "Delivered"),
        )
    courier_sending_person = models.CharField(max_length=100)
    courier_receiving_person = models.CharField(max_length=100)
    receiving_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, help_text='Receiving Branch')
    delivery_address = models.CharField(max_length=100)
    delivery_cost = models.FloatField(default='50', blank=False, help_text='Cost of Courier Service')
    courier_tracking_id = HashidAutoField(primary_key=True)
    received_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    courier_status = models.CharField(choices=STATUS_CHOICES, default='Pending', blank=False, max_length=9, help_text='Status of Courier')


    class Meta:
        ordering = ['received_at']

    def __str__(self):
        return self.courier_name











