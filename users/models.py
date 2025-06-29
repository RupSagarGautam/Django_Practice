from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    class GenderOptions(models.TextChoices):
        Male = 'Male', 'Male'
        Female = 'Female', 'Female'
        Others = 'Others', 'Others'
            
            
    user = models.OneToOneField(User, on_delete=models.CASCADE) #CASCASE Deletes user/ SETNULL - Sets null value
    address = models.CharField(blank=True, null=True, max_length=50)
    phone = models.CharField(blank="True", null=True, max_length=10)
    nationality = models.CharField(blank=True, null=True, max_length=15, default="Nepal")
    gender = models.CharField(choices=GenderOptions, default=GenderOptions.Male, max_length=6)
    profile_image = models.ImageField(blank=True, null=True, upload_to='users')
    dob = models.DateField(blank=True, null=True)
    