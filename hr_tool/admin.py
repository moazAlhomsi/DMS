from django.contrib import admin
from .models import Employee , Salary , Holiday , Absence

# Register your models here.

admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Holiday)
admin.site.register(Absence)