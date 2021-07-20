from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Projects, Ratings, Category
from.forms import RatingForm


# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {}
    projects = Projects.objects.all()
    categories = Category.objects.all()
    context= {'categories': categories, 'projects': projects }


    return render(request, 'index.html',context)

def about(request):

    return render(request, 'about.html')

def upload(request):
    categories = Category.objects.all()
    

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data ['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data ['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data ['category_new'])
        else:
            category = None

        project = Projects.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('home')

    context = {'categories': categories}
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
    return render(request, 'rating.html', context)