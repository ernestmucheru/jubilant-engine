from django.db import models

# Create your models here.
class Projects(models.Model):
    alt = models.CharField(max_length=60)
    image = models.ImageField(upload_to="")
    decription = models.CharField(max_length=300)

    def __str__(self):
        return self.alt