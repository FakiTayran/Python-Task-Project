from django.contrib import admin

# Register your models here.

from .models import Operation
from .models import Bin

admin.site.register(Operation)
admin.site.register(Bin)