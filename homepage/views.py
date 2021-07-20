from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Projects, Ratings
from.forms import RatingForm


# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {}
    projects = Projects.objects.all()
    # categroies = Category.objects.all()
    context["projects"] = projects 


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

@login_required

def rating(request, id):
    Project = Projects.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = Ratings(
                author = user,
                project = Project,
                design_rating = form.cleaned_data["design_rating"],
                usability_rating = form.cleaned_data["usability_rating"],
                content_rating = form.cleaned_data["content_rating"],
                comment = form.cleaned_data["comment"],
            )
            rating.save()
    else:
        form = RatingForm()
    ratings = Ratings.objects.filter(project=Project).order_by('-created_on')
    context={
        'project' : Project,
        'form' : form,
        "ratings": ratings,
    }
    return render(request, 'rating.html', context)@login_required