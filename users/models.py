# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('normal', 'Normal User'),
    ]       
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='normal')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related name to avoid clashes
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Custom related name to avoid clashes
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user_permissions',
    )

    @property
    def activate(self):
        self.is_active = True
        self.save()
    
    @property
    def deactivate(self):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.username
