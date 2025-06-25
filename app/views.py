from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def aboutme(request):
    return render(request, 'app/aboutme.html')

def skills(request):
   return render(request, 'app/skills.html')

def projects(request):
    return render(request, 'app/projects.html')

def contact(request):
   return render(request, 'app/contact.html')
