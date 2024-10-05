from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # This will import all the fields that we need from User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    profile_url = models.URLField(blank= True)
    profile_picture = models.ImageField(blank= True, upload_to="profile_pics")

    def __str__(self):
        return self.user.username