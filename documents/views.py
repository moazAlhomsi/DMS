# documents/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Document
from .forms import DocumentUploadForm

@method_decorator(login_required, name='dispatch')
class DocumentUploadView(View):
    def get(self, request):
        form = DocumentUploadForm()
        return render(request, 'documents/upload.html', {'form': form})

    def post(self, request):
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            document.save()
            return redirect('document_list')
        return render(request, 'documents/upload.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class DocumentListView(View):
    def get(self, request):
        documents = Document.objects.filter(is_private=False)  # Public documents
        if request.user.is_authenticated:
            private_docs = Document.objects.filter(uploaded_by=request.user, is_private=True)
            documents = documents | private_docs
        return render(request, 'documents/list.html', {'documents': documents})
