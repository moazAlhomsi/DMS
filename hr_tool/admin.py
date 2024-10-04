from django.contrib import admin
from .models import Employee , Holiday , Absence , Recruitment

# Register your models here.

admin.site.register(Employee)
admin.site.register(Holiday)
admin.site.register(Absence)
admin.site.register(Recruitment)