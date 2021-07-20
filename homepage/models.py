from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,null=False ,blank=False)

    def __str__(self):
        return self.name

class Projects(models.Model):
    alt = models.CharField(max_length=60)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="",null=False, blank=False)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.alt

class Ratings(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    design_rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability_rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    content_rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.author
