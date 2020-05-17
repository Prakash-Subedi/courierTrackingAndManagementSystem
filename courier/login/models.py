from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    POST_CHOICES = (
        ("Manager", "Manager"),
        ("Staff", "Staff"),
    )
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    post = models.CharField(choices=POST_CHOICES, max_length=20)
    branch = models.ForeignKey('courier_branch.Branch', on_delete=models.CASCADE)
    # branch = models.CharField(max_length=100)
    age = models.IntegerField()


    def __str__(self):
        return self.user.username