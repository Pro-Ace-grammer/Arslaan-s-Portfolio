from django.shortcuts import render
from .models import *

# Create your views here

def index(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    resume = Resume.objects.all().last()
    return render(request,'index.html',{
        'education':education,
        'experience':experience,
        'skills':skills,
        'projects':projects,
        'resume':resume
    })