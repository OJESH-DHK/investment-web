from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Projects, Services, BlogDetails, Contact ,Team , Testimonial,Faq
from django.contrib.auth import authenticate, login, logout


@login_required
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
            return redirect('ad_service')  # Redirect to clear the form or show success
    return render(request,'admin/service/ad_addservice.html')





def ad_editservice(request, id):
    service = get_object_or_404(Services, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        # Update fields
        service.title = title
        service.content = content

        # If a new image is uploaded, update it
        if image:
            service.image = image

        service.save()  # Save changes to DB
        return redirect('ad_service')  # Redirect to service list or detail page

    return render(request, 'admin/service/ad_editservice.html', {
        'service': service 
    })

def delete_service(request, id):
    service = get_object_or_404(Services, id=id)
    if request.method == 'POST':
        service.delete()
    return redirect('ad_service')


#admin blog
def ad_blog(request):
    blogs = BlogDetails.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request,'admin/blog/ad_blog.html',context)


def ad_addblog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content', 'This is default content')
        image = request.FILES.get('image')

        if title and description and image:
            BlogDetails.objects.create(
                title=title,
                description=description,
                content=content,
                image=image,
                author="Admin"  # or dynamically: request.user.username if using authentication
            )
            return redirect('ad_blog')  # Replace with your actual blog list view name

    return render(request, 'admin/blog/ad_addblog.html', {
        'action': 'Add',
        'blog': {}
    })

def delete_blog(request, id):
    blog = get_object_or_404(BlogDetails, id=id)
    if request.method == 'POST':
        blog.delete()
    return redirect('ad_blog')




def ad_editblog(request, id):
    blog = get_object_or_404(BlogDetails, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        author= request.POST.get('author')

        blog.title = title
        blog.description = description
        blog.content = content
        blog.author = author

        if image:
            blog.image = image

        blog.save()
        return redirect('ad_blog')  # Adjust to your blog lis hi this is me 

    return render(request, 'admin/blog/ad_editblog.html', {'blog': blog, 'action': 'Edit'})




#admin contact
def ad_contact(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request,'admin/contact/ad_contact.html',context)


def ad_editcontact(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Update fields
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message

        contact.save()
        return redirect('ad_contact')  # Replace with the actual name of your contact list view

    return render(request, 'admin/contact/ad_editcontact.html', {'contact': contact, 'action': 'Edit'})


def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
    return redirect('ad_contact')


def ad_addcontact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            return redirect('ad_contact')  # Update with your contact list view name

    return render(request, 'admin/contact/ad_addcontact.html', {
        'action': 'Add',
        'contact': {}
    })






#admin team
def ad_team(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request,'admin/team/ad_team.html',context)

def delete_team(request, id):
    team = get_object_or_404(Team, id=id)
    if request.method == 'POST':
        team.delete()
    return redirect('ad_team')

def ad_addteam(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        instagram_link = request.POST.get('instagram_link')
        facebook_link = request.POST.get('facebook_link')
        twitter_link = request.POST.get('twitter_link')
        image = request.FILES.get('image')  # For file input

        if name and position and image:
            Team.objects.create(
                name=name,
                position=position,
                image=image,
                instagram_link=instagram_link,
                facebook_link=facebook_link,
                twitter_link=twitter_link
            )
            return redirect('ad_team')  # Replace with your team list view name

    return render(request, 'admin/team/ad_addteam.html', {
        'action': 'Add',
        'team': {}
    })

def ad_editteam(request, id):
    team = get_object_or_404(Team, id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        instagram_link = request.POST.get('instagram_link')
        facebook_link = request.POST.get('facebook_link')
        twitter_link = request.POST.get('twitter_link')
        image = request.FILES.get('image')

        # Update fields
        team.name = name
        team.position = position
        team.instagram_link = instagram_link
        team.facebook_link = facebook_link
        team.twitter_link = twitter_link

        if image:
            team.image = image  # Only update image if a new one is uploaded

        team.save()
        return redirect('ad_team')  # Replace with your team list view name

    return render(request, 'admin/team/ad_editteam.html', {
        'team': team,
        'action': 'Edit'
    })


#admin feedback
def ad_feedback(request):
    feedbacks = Testimonial.objects.all()
    context = {
        'feedbacks': feedbacks,
    }
    return render(request,'admin/feedback/ad_feedback.html',context)


def delete_feedback(request, id):
    feedback = get_object_or_404(Testimonial, id=id)  # FIX: Use Testimonial
    if request.method == 'POST':
        feedback.delete()
    return redirect('ad_feedback')



def ad_addfeedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if name and position and description and image:
            Testimonial.objects.create(
                name=name,
                position=position,
                description=description,
                image=image
            )
            return redirect('ad_feedback')

    return render(request, 'admin/feedback/ad_addfeedback.html', {
        'action': 'Add',
        'testimonial': {}
    })



def ad_editfeedback(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Update fields
        testimonial.name = name
        testimonial.position = position
        testimonial.description = description

        if image:
            testimonial.image = image  # Only update image if a new one is uploaded

        testimonial.save()
        return redirect('ad_feedback')  # Adjust if your feedback list view uses a different name

    return render(request, 'admin/feedback/ad_editfeedback.html', {
        'testimonial': testimonial,
        'action': 'Edit'
    })




#admin faq
def ad_faq(request):
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request,'admin/faq/ad_faq.html',context)

def ad_addfaq(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')

        if title and description and content:
            Faq.objects.create(
                title=title,
                description=description,
                content=content
            )
            return redirect('ad_faq')  # Make sure this matches your URL name for listing FAQs

    return render(request, 'admin/faq/ad_addfaq.html', {
        'action': 'Add',
        'faq': {}
    })

def ad_editfaq(request, id):
    faq = get_object_or_404(Faq, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')

        # Update fields
        faq.title = title
        faq.description = description
        faq.content = content

        faq.save()
        return redirect('ad_faq')  # Adjust if your FAQ list view uses a different name

    return render(request, 'admin/faq/ad_editfaq.html', {
        'faq': faq,
        'action': 'Edit'
    })

def delete_faq(request, id):
    faq = get_object_or_404(Faq, id=id)
    if request.method == 'POST':
        faq.delete()
    return redirect('ad_faq')


def calc(request):
    return render(request,'calc/calc.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')  # Change to your admin dashboard URL name
        else:
            return render(request, 'admin_login/admin_login.html', {'error': 'Invalid credentials or not authorized.'})
    
    return render(request, 'admin_login/admin_login.html')


def admin_logout(request):
    logout(request)
    return redirect('index')















