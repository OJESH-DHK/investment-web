from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

from .models import Projects, Services, BlogDetails, Contact ,Team , Testimonial,Faq


def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def admin_dashboard(request):
    context = {
        'total_projects': Projects.objects.count(),
        'total_services': Services.objects.count(),
        'total_blogs': BlogDetails.objects.count(),
        'total_messages': Contact.objects.count(),
        'total_teams': Team.objects.count(),
        'total_feedback': Testimonial.objects.count(),
        'total_faqs': Faq.objects.count(),
    }

    return render(request, 'admin/admin_dashboard.html', context)



def admin_editproject(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
    }
    
    return render(request,'admin/project/admin_editproject.html',context)


def admin_addproject(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        Projects.objects.create(title=title, content=content, image=image)
        return redirect('admin_editproject')

    return render(request, 'admin/project/admin_addproject.html', {'action': 'Add', 'project': {}})

def delete_project(request, id):
    project = get_object_or_404(Projects, id=id)
    if request.method == 'POST':
        project.delete()
    return redirect('admin_editproject')


def admin_editproject_form(request, id):
    project = get_object_or_404(Projects, id=id)

    if request.method == 'POST':
        # Get data from the submitted form
        project.title = request.POST.get('title')
        project.content = request.POST.get('content')

        # Handle image update if a new image was uploaded
        if 'image' in request.FILES:
            project.image = request.FILES['image']

        # Save updated project to database
        project.save()

        # Redirect to the project list page (or wherever you want)
        return redirect('admin_editproject')

    # If GET request, render the edit form with current project data
    return render(request, 'admin/project/admin_editproject_form.html', {'project': project})\


#admin services
def ad_service(request):
    services = Services.objects.all()
    context = {
        'services': services,
    }
    return render(request,'admin/service/ad_service.html',context)


def ad_addservice(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content', 'This is default content')
        image = request.FILES.get('image')

        if title and image:
            Services.objects.create(
                title=title,
                content=content,
                image=image
            )
            return redirect('ad_addservice')  # Redirect to clear the form or show success
    return render(request,'admin/service/ad_addservice.html')

def ad_editservice(request):
    return render(request,'admin/service/ad_editservice.html')


#admin blog
def ad_blog(request):
    blogs = BlogDetails.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request,'admin/blog/ad_blog.html',context)

def ad_editblog(request):
    return render(request,'admin/service/aad_editblog.html')

#admin contact
def ad_contact(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request,'admin/contact/ad_contact.html',context)

#admin team
def ad_team(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request,'admin/team/ad_team.html',context)

#admin feedback
def ad_feedback(request):
    feedbacks = Testimonial.objects.all()
    context = {
        'feedbacks': feedbacks,
    }
    return render(request,'admin/feedback/ad_feedback.html',context)

#admin faq
def ad_faq(request):
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request,'admin/faq/ad_faq.html',context)














