from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def faq(request):
    return render(request, 'faq.html')
def index(request):
    return render(request, 'index.html')
def projects(request):
    return render(request, 'projects.html')
def services(request):
    return render(request, 'services.html')
def team(request):
    return render(request, 'team.html')
def testimonials(request):
    return render(request, 'testimonials.html')
