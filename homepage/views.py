from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Projects


# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {}
    projects = Projects.objects.all()
    context["projects"] = projects


    return render(request, 'index.html',context)
def about(request):

    return render(request, 'about.html')
def contact(request):

    return render(request, 'contact.html')
