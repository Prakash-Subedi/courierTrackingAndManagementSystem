from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# from courier.courier_branch.models import Comments


class UserProfile(models.Model):
    POST_CHOICES = (
        ("Manager", "Manager"),
        ("Staff", "Staff"),
        ("Admin", "Admin")
        ,
    )
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    post = models.CharField(choices=POST_CHOICES, max_length=20)
    branch = models.ForeignKey('courier_branch.Branch', on_delete=models.CASCADE)
    # branch = models.CharField(max_length=100)
    age = models.IntegerField()


    def __str__(self):
        return self.user.username

class Notice(models.Model):
    topic = models.CharField(max_length=50, blank=False,help_text='Subject/Heading of Notice')
    details = models.TextField(max_length=1000, blank=False,help_text='Details about notice')
    date = models.DateTimeField(auto_now=True)   # last update date auto changes/added

    def __str__(self):
        return self.topic