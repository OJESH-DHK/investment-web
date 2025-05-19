from .models import Organization

def organization_details(request):
    org = Organization.objects.first()  
    return {'org': org}
