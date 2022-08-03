from django.contrib import admin

# Register your models here.
from .models import NavigationRecord
from .models import Vehicle

admin.site.register(NavigationRecord)
admin.site.register(Vehicle)