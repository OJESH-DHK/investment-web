from django.shortcuts import render
from .models import Services
from .models import Projects
from .models import BlogDetails
from .models import Team
from .models import Testimonial
from .models import Faq

# Create your views here.
def about(request):
    teams = Team.objects.all()
    context = {

        'teams' : teams,
    }
    return render(request, 'about.html', context)
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def faq(request):
    return render(request, 'faqs.html')
def index(request):
    services = Services.objects.all()
    projects = Projects.objects.all()
    blogs = BlogDetails.objects.all()
    teams = Team.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = Faq.objects.all()
    

    context = {
        'services': services,
        'projects': projects,
        'blogs' : blogs,
        'teams' : teams,
        'testimonials' : testimonials,
        'faqs': faqs,
    }
    return render(request, 'index.html', context)
def projects(request):
    projects = Projects.objects.all()
    faqs = Faq.objects.all()
    context = {
        'projects': projects,
        'faqs': faqs,
    }
    return render(request, 'project.html',context)
def services(request):
    services = Services.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = Faq.objects.all()
    context = {
        'services': services,
        'testimonials' : testimonials,
        'faqs': faqs,
    }
    return render(request, 'service.html', context)

def team(request):
    return render(request, 'team.html')
def testimonials(request):
    return render(request, 'testimonial.html')

def fourzerofour(request):
    return render(request,'404.html')
