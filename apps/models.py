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




