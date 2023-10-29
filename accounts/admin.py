from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Resources)
admin.site.register(Product)
admin.site.register(Person)