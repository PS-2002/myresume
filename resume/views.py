from django.shortcuts import render, redirect
from .models import Experience, Details, Skills, Projects, Certificates

# Create your views here.
def resume(request):
    details = Details.objects.all()
    return render(request, 'resume/resume.html', {'details':details})


def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'resume/experience.html', {'experiences':experiences})


def skills(request):
    skills = Skills.objects.all()
    return render(request, 'resume/skills.html', {'skills': skills})


def education(request):
    return render(request, 'resume/education.html')


def projects(request):
    projects = Projects.objects.all()
    return render(request, 'resume/projects.html', {'projects': projects})


def certificates(request):
    certificates = Certificates.objects.all()
    return render(request, 'resume/certificates.html', {'certificates': certificates})
