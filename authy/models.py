from django.db import models
from django.contrib.auth.models import User
from homepage.models import Projects
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    name = models.CharField(max_length=100,null=True)
    bio = models.CharField(max_length=100,null=True)
    joined = models.DateTimeField(auto_now_add=True,null=True)

    def __str__name(self):
        return f'{self.user.username} Profile'

