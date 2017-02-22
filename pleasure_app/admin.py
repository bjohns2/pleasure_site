from django.contrib import admin

# Register your models here.

from .models import Educator
from .models import Training
from .models import Presentation

admin.site.register(Educator)
admin.site.register(Training)
admin.site.register(Presentation)

