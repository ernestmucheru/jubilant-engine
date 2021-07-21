from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('project/<int:id>/', views.viewProject, name='project'),
    path('upload', views.upload, name='upload'),
    path('rating/<int:id>/', views.rating, name='rating'),
    path('searchCategory', views.searchCategory, name='searchCategory'),
]

if settings.DEBUG:
    urlpatterns += static(
       settings.STATIC_URL,
       document_root=settings.STATIC_ROOT)
    urlpatterns += static(
       settings.MEDIA_URL,
       document_root=settings.MEDIA_ROOT)
