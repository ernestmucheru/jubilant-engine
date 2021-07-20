from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=100,null=True)
    bio = models.CharField(max_length=100,null=True)
    joined = models.DateTimeField(auto_now_add=True,null=True)

    def __str__name(self):
        return f'{self.user.username} Profile'