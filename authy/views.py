from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account for {username} has been created successfully')
            return redirect('login')


    context = {'form':form}
    return render(request,'accounts/register.html', context)
def loginPage(request):
    context = {}
    return render(request,'accounts/login.html', context)
