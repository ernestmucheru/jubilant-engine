from django.contrib import admin
from .models import Projects,Category,Ratings
# Register your models here.


admin.site.register(Projects)
admin.site.register(Category)
admin.site.register(Ratings)