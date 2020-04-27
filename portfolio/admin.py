from django.contrib import admin

# Register your models here.
 
from .models import Portfolio

admin.site.register(Portfolio)

from .models import MainImage

admin.site.register(MainImage)