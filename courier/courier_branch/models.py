from django.db import models
from hashid_field import HashidAutoField   # pip install django-hashid-field
from phone_field import PhoneField  # pip install django-phone-field


# Create your models here.



# branch.

class Branch(models.Model):
    branch_name = models.CharField(max_length=30, blank=False, unique=True)
    branch_address = models.CharField(max_length=50, blank=False)
    branch_phone_no = models.CharField(blank=True, max_length=16, help_text='Contact phone number')
    branch_des = models.TextField()
    branch_pic = models.ImageField(upload_to='img/', blank=True)  # python -m pip install Pillow
    branch_created_at = models.DateTimeField(auto_now_add=True)
    branch_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branch_name

# Branch_CHOICE = ( Branch.objects.only('branch_name'))

# courier main class



class Courier(models.Model):
    courier_id = models.AutoField(primary_key=True)  # auto generated
    courier_name = models.CharField(max_length=100, help_text='Enter name of courier')
    courier_description = models.TextField(max_length=300, blank=True, help_text='Notes about Courier')
    sending_branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, help_text='Sending Branch ')




# courier base class for more details

class CourierDetails(Courier):
    courier_sending_person = models.CharField(max_length=100)
    courier_receiving_person = models.CharField(max_length=100)
    receiving_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, help_text='Receiving Branch')
    delivery_address = models.CharField(max_length=100)
    delivery_cost = models.FloatField(default='50', blank=False, help_text='Cost of Courier Service')
    courier_tracking_id = HashidAutoField(primary_key=True)
    received_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    courier_status = models.CharField(default='Pending', blank=False, max_length=9, help_text='Status of Courier')


    class Meta:
        ordering = ['received_at']

    def __str__(self):
        return self.courier_name











