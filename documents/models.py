# documents/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Document(models.Model):
    FILE_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
        # Add more types if needed
    ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    is_private = models.BooleanField(default=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-detect file type
        if self.file.name.endswith(('jpg', 'jpeg', 'png', 'gif')):
            self.file_type = 'image'
        elif self.file.name.endswith(('mp4', 'mkv', 'avi')):
            self.file_type = 'video'
        elif self.file.name.endswith(('mp3', 'wav')):
            self.file_type = 'audio'
        elif self.file.name.endswith(('pdf', 'doc', 'docx', 'txt')):
            self.file_type = 'document'
        else:
            self.file_type = 'document'  # Default to document if unknown
        super().save(*args, **kwargs)
