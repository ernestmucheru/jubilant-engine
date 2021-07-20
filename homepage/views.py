from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Projects


# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {}
    projects = Projects.objects.all()
    # categroies = Category.objects.all()
    context["projects"] = projects = {'projects': projects}


    return render(request, 'index.html',context)

def about(request):

    return render(request, 'about.html')

def upload(request):
    projects = Projects.objects.all()
    context = {'projects':projects}

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        print('data:', data)
        print('image:', image)

    return render(request, 'upload.html',context)

def viewProject(request, id):
    project = Projects.objects.get(id=id)
    return render(request, 'single.html',{'project':project})

def contact(request): 

    return render(request, 'contact.html')
