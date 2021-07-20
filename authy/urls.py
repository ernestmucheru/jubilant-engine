from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    

]
if settings.DEBUG:
    urlpatterns += static(
       settings.STATIC_URL,
       document_root=settings.STATIC_ROOT)
    urlpatterns += static(
       settings.MEDIA_URL,
       document_root=settings.MEDIA_ROOT)
