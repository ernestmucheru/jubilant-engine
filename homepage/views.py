from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Projects,Category,Rating
from authy.models import Profile
from.forms import RateForm



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


def rating(request,id):
    user = Profile.objects.get(user= request.user)
    project = Projects.objects.get(id=id)
    ratings=Rating.objects.filter(project = project).last()
    tech_tags = project.technologies.split(",")
    try:
        rates = Rating.objects.filter(user=user,project=project).first()
    except Rating.DoesNotExist:
        rates=None
    if rates is None:
        rates_status=False
    else:
        rates_status = True
    form = RateForm()
    rating=None
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.project = project
            rate.save()
        try:
            rating = Rating.objects.filter(project_id=id)
        except Rating.DoesNotExist:
            rating=None
        design = form.cleaned_data['design']
        usability = form.cleaned_data['usability']
        content = form.cleaned_data['content']
        rate.average = (design + usability + content)/2
        rate.save()
        design_ratings = [d.design for d in rating]
        design_average = sum(design_ratings) / len(design_ratings)
        usability_ratings = [us.usability for us in rating]
        usability_average = sum(usability_ratings) / len(usability_ratings)
        content_ratings = [content.content for content in rating]
        content_average = sum(content_ratings) / len(content_ratings)
        score = (design_average + usability_average + content_average) / 3
        rate.design_average = round(design_average, 2)
        rate.usability_average = round(usability_average, 2)
        rate.content_average = round(content_average, 2)
        rate.score = round(score, 2)
        rate.save()
        return redirect("projects", id=project.id)
    else:
        form = RateForm()
    ctx={
        "project":project,
        "ratings":ratings,
        "form":form,
        "tech_tags":tech_tags,
        "rates_status":rates_status
    }
    return render(request,"projects.html",ctx)

def searchCategory(request):
    if request.method == "POST":
        searched = request.POST['searched']
        category = Category.objects.filter(name__contains=searched)
        return render(request,"results.html", {"searched":searched, "category":category} )
    else:
        return render(request,"results.html", {})
