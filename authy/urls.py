from django.urls import path
from . import views

app_name = "authy"

urlpatterns = [
    # path("",views.homepage, name="homepage"),
    path("register", views.register, name="register"),
    path("login", views.login_request, name="login"),

    
]