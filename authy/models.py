from django.db import models
from django.contrib.auth.models import User
from homepage.models import Projects

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=100,null=True)
    bio = models.CharField(max_length=100,null=True)
    joined = models.DateTimeField(auto_now_add=True,null=True)

    def __str__name(self):
        return f'{self.user.username} Profile'

# class Rating(models.Model):
#     rating = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#         (6, '6'),
#         (7, '7'),
#         (8, '8'),
#         (9, '9'),
#         (10, '10'),
#     )
#     design = models.IntegerField(choices=rating, default=0, blank=True)
#     usability = models.IntegerField(choices=rating, blank=True)
#     content = models.IntegerField(choices=rating, blank=True)
#     score = models.FloatField(default=0, blank=True)
#     design_average = models.FloatField(default=0, blank=True)
#     usability_average = models.FloatField(default=0, blank=True)
#     content_average = models.FloatField(default=0, blank=True)
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='rater')
#     project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='ratings', null=True)
#     rated_at=models.DateTimeField(auto_now_add=True)
#     def save_rating(self):
#         self.save()
    
#     def delete_rating(self):
#         self.delete()
#     @classmethod
#     def get_project_rating(cls, pk):
#         rating = Rating.objects.filter(project_id=pk).all()
#         return rating
#     def __str__(self):
#         return f'{self.project} Rating'