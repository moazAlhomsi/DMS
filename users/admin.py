from django.contrib import admin
from .models import User , Settings
from django.contrib.auth.admin import UserAdmin


# Register your models here.

# customizing the User model required customizing the user admin
class CustomUserAdmin(UserAdmin):
    # show selected fields as a table
    list_display = ['id', 'email','username', 'is_staff','is_superuser']    
    ordering = ['-id']

    # grouping the fields in the user info page
    fieldsets = (
        (None, 
                {'fields':('email', 'password',)}
            ),
            ('User Information',
                {'fields':('username', 'first_name', 'last_name' , 'image')}
            ),
            ('Permissions', 
                {'fields':('is_staff', 'is_superuser', 'is_active', 'groups','user_permissions')}
            ),
            ('Registration', 
                {'fields':('date_joined', 'last_login',)}
        )
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Settings)