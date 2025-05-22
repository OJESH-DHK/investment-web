from django.contrib import admin

# Register your models here.
from .models import Services
from .models import Projects
from .models import BlogDetails
from .models import Team
from .models import Testimonial
from .models import Faq
from .models import Contact
from .models import Organization
from .models import InvestmentSetting
from .models import Slider

admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(BlogDetails)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Faq)
admin.site.register(Contact)
admin.site.register(Organization)
admin.site.register(InvestmentSetting)
admin.site.register(Slider)




