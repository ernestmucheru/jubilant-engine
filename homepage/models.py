from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
from authy.models import Profile
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,null=False ,blank=False)

    def __str__(self):
        return self.name

class Projects(models.Model):
    alt = models.CharField(max_length=60)
    title = models.CharField(max_length=100, null=True)
    image = CloudinaryField('image')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    link = models.CharField(max_length=400, null=True, blank=True)
    def __str__(self):
        return self.alt



class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='ratings', null=True)
    rated_at=models.DateTimeField(auto_now_add=True)
    def save_rating(self):
        self.save()
    
    def delete_rating(self):
        self.delete()
    @classmethod
    def get_project_rating(cls, pk):
        rating = Rating.objects.filter(project_id=pk).all()
        return rating
    def __str__(self):
        return f'{self.project} Rating'

