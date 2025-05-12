from django.contrib import admin

# Register your models here.
from .models import Services
from .models import Projects
from .models import BlogDetails
from .models import Team
from .models import Testimonial

admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(BlogDetails)
admin.site.register(Team)
admin.site.register(Testimonial)


