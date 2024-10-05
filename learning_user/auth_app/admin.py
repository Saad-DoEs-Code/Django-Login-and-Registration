from django.contrib import admin
from auth_app.models import UserProfileInfo

# Register your models here.
admin.site.register(UserProfileInfo) # Since it is in One-to-One Relationship with the User Model, therefore, there is no need to register User Model separately
