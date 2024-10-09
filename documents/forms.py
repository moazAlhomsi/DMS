# documents/forms.py

from django import forms
from .models import Document, DocumentGroup


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file', 'is_private' , 'language']

class DocumentReplaceForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'is_private']



class DocumentSelectionForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['selected']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)



class DocumentGroupForm(forms.ModelForm):
    class Meta:
        model = DocumentGroup
        fields = ['name']

class DocumentRequestForm(forms.Form):
    recipient_email = forms.EmailField(label='البريد الإلكتروني للمستلم')
    document_id = forms.IntegerField(widget=forms.HiddenInput())