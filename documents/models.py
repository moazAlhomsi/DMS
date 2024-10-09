# documents/models.py

from django.db import models
from django.contrib.auth import get_user_model
# from django.utils.text import humanize
import re

User = get_user_model()

class Document(models.Model):
    FILE_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
        ('txt','Text')
        
        # Add more types if needed
    ]

    LANGUAGES = [
        ('en', 'English'),
        ('ar', 'Arabic'),

    ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    is_private = models.BooleanField(default=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    selected = models.BooleanField(default=False)
    comment = models.TextField( null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField()
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    details = models.TextField(blank=True, null=True) 

      
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-detect file type
        if self.file.name.endswith(('jpg', 'jpeg', 'png', 'PNG','gif')):
            self.file_type = 'image'
        elif self.file.name.endswith(('mp4', 'mkv', 'avi')):
            self.file_type = 'video'
        elif self.file.name.endswith(('mp3', 'wav', 'ogg' , 'm4a', 'acc')):
            self.file_type = 'audio'
        elif self.file.name.endswith(('csv',  'xlsx')):
            self.file_type = 'document_Excel'
        elif self.file.name.endswith(('ppt', 'pptx')):
            self.file_type = 'document_PowePoint'
        elif self.file.name.endswith(('doc', 'docx')):
                self.file_type = 'document_word'
        elif self.file.name.endswith(('pdf')):
            self.file_type = 'document_Pdf'
        elif self.file.name.endswith(('txt')):
                self.file_type = 'document_txt'

        else:
            self.file_type = 'unknown_document'  # Default to document if unknown
        super().save(*args, **kwargs)


    def has_access(self, user):
        # Check user permissions here 
        if user.is_superuser or self.uploaded_by == user:
            return True
        return False
    
    def is_gif(self):
        filename = self.file.name  # احصل على اسم الملف
        return filename.endswith('.gif')



class DocumentGroup(models.Model):
    name = models.CharField(max_length=200)
    documents = models.ManyToManyField(Document, related_name='groups')

    def __str__(self):
        return self.name


    



