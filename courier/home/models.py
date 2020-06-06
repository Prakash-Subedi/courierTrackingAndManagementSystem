from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=15)
    messsage = models.TextField(max_length=300)

    def __str__(self):
        return self.full_name