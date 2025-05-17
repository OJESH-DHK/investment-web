from django import forms
from .models import Contact
from .models import Projects

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


#admin dashboard

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'content', 'image']
