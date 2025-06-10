from django.shortcuts import render, get_object_or_404

from .models import Services
from .models import Projects
from .models import BlogDetails
from .models import Slider
from .models import Team
from .models import Testimonial
from .models import Faq, About
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect



# Create your views here.
def about(request):
    teams = Team.objects.all()
    about = About.objects.first()
    context = {

        'teams' : teams,
        'about': about,
    }
    return render(request, 'about.html', context)


def blog(request):
    blogs = BlogDetails.objects.all()
    context={
        'blogs':blogs
    }
    return render(request, 'blog.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def faq(request):
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'faqs.html',context)



def index(request):
    services = Services.objects.all()
    projects = Projects.objects.all()
    blogs = BlogDetails.objects.all()
    teams = Team.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = Faq.objects.all()
    sliders = Slider.objects.all()
    about = About.objects.first()
    context = {
        'services': services,
        'projects': projects,
        'blogs' : blogs,
        'teams' : teams,
        'testimonials' : testimonials,
        'faqs': faqs,
        'sliders': sliders,
        'about': about,
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

def service_detail(request, id):
    service = get_object_or_404(Services, id=id)
    return render(request, 'service_detail.html', {'service': service})

def team(request):
    teams = Team.objects.all()
    context = {
        'teams' : teams,

    }
    return render(request, 'team.html',context)


def testimonials(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials' : testimonials,
    }
    return render(request, 'testimonial.html',context)

def fourzerofour(request):
    return render(request,'404.html')











