from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,null=False ,blank=False)

    def __str__(self):
        return self.name

class Projects(models.Model):
    alt = models.CharField(max_length=60)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="")
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.alt

