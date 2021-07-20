from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from homepage.models import Projects
# from .models import Rating, Profile
# from .forms import RateForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account for ' + user +' has been created successfully')
                return redirect('login')


        context = {'form':form}
        return render(request,'accounts/register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Username OR Password is incorrect')
        context = {}
        return render(request,'accounts/login.html', context)

def logoutUser(request):
    return redirect('login')

def profile(request):

    return render(request, 'profile.html')

# def projects(request,id):
#     user = Profile.objects.get(user= request.user)
#     project = Projects.objects.get(id=id)
#     ratings=Rating.objects.filter(project = project).last()
#     tech_tags = project.technologies.split(",")
#     try:
#         rates = Rating.objects.filter(user=user,project=project).first()
#     except Rating.DoesNotExist:
#         rates=None
#     if rates is None:
#         rates_status=False
#     else:
#         rates_status = True
#     form = RateForm()
#     rating=None
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             rate = form.save(commit=False)
#             rate.user = user
#             rate.project = project
#             rate.save()
#         try:
#             rating = Rating.objects.filter(project_id=id)
#         except Rating.DoesNotExist:
#             rating=None
#         design = form.cleaned_data['design']
#         usability = form.cleaned_data['usability']
#         content = form.cleaned_data['content']
#         rate.average = (design + usability + content)/2
#         rate.save()
#         design_ratings = [d.design for d in rating]
#         design_average = sum(design_ratings) / len(design_ratings)
#         usability_ratings = [us.usability for us in rating]
#         usability_average = sum(usability_ratings) / len(usability_ratings)
#         content_ratings = [content.content for content in rating]
#         content_average = sum(content_ratings) / len(content_ratings)
#         score = (design_average + usability_average + content_average) / 3
#         rate.design_average = round(design_average, 2)
#         rate.usability_average = round(usability_average, 2)
#         rate.content_average = round(content_average, 2)
#         rate.score = round(score, 2)
#         rate.save()
#         return redirect("projects", id=project.id)
#     else:
#         form = RateForm()
#     ctx={
#         "project":project,
#         "ratings":ratings,
#         "form":form,
#         "tech_tags":tech_tags,
#         "rates_status":rates_status
#     }
#     return render(request,"projects.html",ctx)