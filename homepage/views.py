from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


# Create your views here.
@login_required(login_url='login')
def index(request):

    return render(request, 'index.html')
def about(request):

    return render(request, 'about.html')
def contact(request):

    return render(request, 'contact.html')
