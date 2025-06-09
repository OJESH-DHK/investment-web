from django.db import models

# Create your models here.
class Services(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField(default="This is default content")
    image=models.ImageField(upload_to='services_images/')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-id']

class Projects(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField(default="This is default content")
    image=models.ImageField(upload_to='project_images/')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-id']

class BlogDetails(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField(default="This is default content")
    image=models.ImageField(upload_to='blog_images/')
    created_at =models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=100,default="Admin")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-id']

class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.TextField()
    image = models.ImageField(upload_to='Team/')
    instagram_link = models.URLField(blank=True, null=True) 
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    position = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='Testimonial/')

    def __str__(self):
        return self.name
    
class Faq(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField(default="This is default content")
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)  # Corrected from models.models.CharField to models.CharField
    email = models.EmailField()  # Corrected 'emaai' to 'EmailField'
    subject = models.CharField(max_length=200)  # Use CharField for the subject
    message = models.TextField()  # Use TextField for the message
    

    def __str__(self):
        return self.name
    
class Organization(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    gmail = models.EmailField()
    
    # Social media links
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    logo = models.ImageField(upload_to='org_logos/')

    def __str__(self):
        return self.name

# models.py
from django.db import models

class InvestmentSetting(models.Model):
    return_rate = models.FloatField(default=10.0, help_text="Return rate in percentage (e.g., 10 for 10%)")

    def __str__(self):
        return f"Return Rate: {self.return_rate}%"

class Slider(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Slider/')

    def __str__(self):
        return self.title


class About(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    total_users = models.PositiveIntegerField()
    projects_completed = models.PositiveIntegerField()
    years_experience = models.PositiveIntegerField()
    team_members = models.PositiveIntegerField()
    
    agenda_1 = models.CharField(max_length=255)
    agenda_2 = models.CharField(max_length=255)
    agenda_3 = models.CharField(max_length=255)
    agenda_4 = models.CharField(max_length=255)

    def __str__(self):
        return self.title









