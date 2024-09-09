from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, ProjectsForm, ExperienceForm, CertificatesForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def owner_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'])
            if user is not None:
                login(request, user)
                return render(request, 'owner/login_done.html')
            else:
                return render(request, 'owner/login_failed.html')
    else:
        form = LoginForm()
    return render(request, 'owner/login.html', {'form': form})

def owner_logout(request):
    logout(request)
    return redirect('login')

@login_required
def edit_project(request):
    if request.method == 'POST':
        form = ProjectsForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume') 
    else:
        form = ProjectsForm()

    return render(request, 'owner/edit_project.html', {'form': form})


@login_required
def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = ExperienceForm()

    return render(request, 'owner/add_experience.html', {'form': form})


@login_required
def add_certificate(request):
    if request.method == 'POST':
        form = CertificatesForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')
    else:
        form = CertificatesForm()

    return render(request, 'owner/add_certificate.html', {'form': form})

