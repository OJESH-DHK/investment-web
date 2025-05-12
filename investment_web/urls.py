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
    path("404/",fourzerofour,name='fourzerofour')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
