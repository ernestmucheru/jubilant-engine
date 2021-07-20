from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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

def upload(request):

    return render(request, 'upload.html')

def viewProject(request, id):
    project = Projects.objects.get(id=id)
    return render(request, 'single.html',{'project':project})

def contact(request): 

    return render(request, 'contact.html')
