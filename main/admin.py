from django.contrib import admin

# Register your models here.
from .models import Equipment,Services

admin.site.register(Equipment)
admin.site.register(Services)

