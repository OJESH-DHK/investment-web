"""
URL configuration for investment_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.views import index,about,blog,contact,faq,projects,services,team,testimonials,fourzerofour 
from apps.admin_views import admin_dashboard

from apps.admin_views import admin_editproject
from apps.admin_views import admin_addproject
from apps.admin_views import delete_project
from apps.admin_views import admin_editproject_form
from apps.admin_views import ad_service
from apps.admin_views import ad_blog
from apps.admin_views import ad_contact
from apps.admin_views import ad_team
from apps.admin_views import ad_feedback
from apps.admin_views import ad_faq, ad_editservice, ad_addservice ,delete_service
from apps.admin_views import ad_addblog ,delete_blog, ad_editblog, ad_editcontact ,delete_contact, ad_addcontact , delete_team , ad_addteam, ad_editteam , delete_feedback , ad_slider ,ad_deleteslider , ad_editslider
from apps.admin_views import ad_addfeedback , ad_editfeedback , ad_addfaq ,ad_editfaq ,delete_faq , calc ,admin_login ,admin_logout, ad_org , edit_organization , ad_investment_list , ad_edit_investment , ad_addslider
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('blog/',blog,name='blog'),
    path('contact/',contact,name='contact'),
    path('faq/',faq,name='faq'),
    path('projects/',projects,name='projects'),
    path('services/',services,name='services'),
    path('team/',team,name='team'),
    path('testimonials/',testimonials,name='testimonials'),
    path("404/",fourzerofour,name='fourzerofour'),

    #admin urls
    path('dashboard/',admin_dashboard,name='admin_dashboard'),
#admin project urls
    path('admin_editproject/', admin_editproject, name='admin_editproject'),
    path('admin_addproject/',admin_addproject,name='admin_addproject'),
    path('projects/delete/<int:id>/', delete_project, name='admin_deleteproject'),
    path('admin_editproject/<int:id>/', admin_editproject_form, name='admin_editproject_form'),
#admin services urls
    path('ad_service/',ad_service,name='ad_service'),
    path('ad_editservice/<int:id>/',ad_editservice,name='ad_editservice'),
    path('ad_addservice',ad_addservice,name='ad_addservice'),
    path('services/delete/<int:id>/', delete_service, name='delete_service'),

#admin blog urls
    path('ad_blog/',ad_blog,name='ad_blog'),
    path('ad_addblog/',ad_addblog,name='ad_addblog'),
    path('blog/delete/<int:id>/',delete_blog , name='delete_blog'),
    path('ad_editblog/<int:id>/',ad_editblog,name='ad_editblog'),


#admin contact urls
    path('ad_contact/',ad_contact,name='ad_contact'),
    path('ad_editcontact/<int:id>/',ad_editcontact,name='ad_editcontact'),
    path('contact/delete/<int:id>/', delete_contact, name='delete_contact'),
    path('ad_addcontact/',ad_addcontact,name='ad_addcontact'),
#admin team urls
    path('ad_team/',ad_team,name='ad_team'),
    path('team/delete/<int:id>/', delete_team, name='delete_team'),
    path('ad_addteam/',ad_addteam,name='ad_addteam'),
    path('ad_editteam/<int:id>/', ad_editteam, name='ad_editteam'),
    
#admin feedback urls
    path('ad_feedback/',ad_feedback,name='ad_feedback'),
    path('delete_feedback/<int:id>/', delete_feedback, name='delete_feedback'),
    path('ad_addfeedback/',ad_addfeedback,name='ad_addfeedback'),
    path('ad_editfeedback/<int:id>/', ad_editfeedback, name='ad_editfeedback'),

#admin faq urls
    path('ad_faq/',ad_faq,name='ad_faq'),
    path('ad_addfaq/',ad_addfaq,name='ad_addfaq'),
    path('ad_editfaq/<int:id>/', ad_editfaq, name='ad_editfaq'),
    path('faq/delete/<int:id>/', delete_faq, name='delete_faq'),
    path('calc/', calc, name='calc'),
    path('admin-login/', admin_login, name='admin_login'),
    path('logout/', admin_logout, name='logout'),

#admin organization details 

    path('ad_org/', ad_org, name='ad_org'),
    path('organization/edit/<int:id>/', edit_organization, name='edit_organization'),


#admin calc investment settings 

    path('ad_investment_list/', ad_investment_list, name='ad_investment_list'),
    path('ad_edit_investment/<int:id>/', ad_edit_investment, name='ad_edit_investment'),

#for sliders 
    path('ad_slider/', ad_slider, name='ad_slider'),
    path('slider/delete/<int:id>/', ad_deleteslider, name='ad_deleteslider'),
    path('slider/add/', ad_addslider, name='ad_addslider'),  
    path('slider/edit/<int:id>/', ad_editslider, name='ad_editslider'),










]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
