from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse,  HttpResponseForbidden
from django.conf import settings
from django.urls import reverse
from .models import Document, DocumentGroup
from .forms import DocumentUploadForm, DocumentReplaceForm,  SearchForm, DocumentGroupForm
import mimetypes, os
from documents.documentsAI import countent_descraption as fu

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
          
            desc = ""
            text = ""
            deta = ""
            # Handle different file types
        # pdf 
            if document.file.name.endswith(('pdf')):
                #Content 
                text = fu.extract_text_from_pdf(document.file)
                document.content = text
                #Details
                deta = fu.details_document(document.file)
                document.details = deta
                #Description
                #desc = fu.summarize_text(text, max_words=150)
                #document.description = desc
        # word 
            elif document.file.name.endswith(('doc', 'docx')):
                #Content
                text = fu.extract_text_from_word(document.file)
                document.content = text
                #Details
                deta = fu.details_document(document.file)
                document.details = deta
                #Description
                # desc = fu.description_Word(document.file)
                # document.description = desc
            
        # Powerpoint
            elif document.file.name.endswith(('ppt', 'pptx')):
                # # Content
                text = fu.extract_text_from_powerpoint(document.file)
                document.content = text
                # Details
                deta = fu.details_document(document.file)
                document.details = deta
                # Description
                # desc = fu.description_powerpoint(document.file)
                # document.description = desc

        # Excel
            elif document.file.name.endswith(('csv',  'xlsx')):
                # Content
                text = fu.extract_text_from_excel(document.file)
                document.content = text
                # Details
                deta = fu.details_excel(document.file)
                document.details = deta
                # Description
                # desc = fu.description_excel(document.file)
                # document.description = desc
         
        # txt 
            elif document.file.name.endswith(('txt')):
                 #Content
                text = fu.extract_text_from_text(document.file)
                document.content = text
                 #Details
                deta = fu.details_document(document.file)
                document.details = deta
                #Description
                # desc = fu.description_txt(document.file)
                # document.description = desc

        # Audio
            elif document.file.name.endswith(('mp3', 'wav', 'ogg', 'm4a')):
                #Content
                text = fu.extract_text_from_audio(document.file)
                document.content = text
                #Details
                deta = fu.details_audio(document.file)
                document.details = deta
                #Description
                # desc = fu.description_audio(document.file)
                # document.description = desc
            
        # Video
            elif document.file.name.endswith(('mp4', 'mkv', 'avi')):
                document.save()
                #Content
                text = fu.extract_text_from_video(document.file)
                document.content = text 
                #Details
                deta = fu.details_video(document.file)
                document.details = deta
                #Description
                # desc = fu.description_video(document.file)
                # document.description = desc
                
        # Image
            elif document.file.name.endswith(('jpg', 'jpeg', 'png','PNG', 'gif')):
                #Content
                desc = fu.extract_text_from_image(document.file)
                document.description = desc
                #Details
                deta = fu.details_image(document.file)
                document.details = deta
                #Description
                # desc = fu.description_image(document.file)
                # document.description = desc
                

            else:
                # Handle unsupported file types
                return render(request, 'documents/upload.html', {'form': form, 'error': 'Unsupported file type'})

            document.save()
            return redirect('document_list')
        
        return render(request, 'documents/upload.html', {'form': form})

    def view_document_content(request, document_id):
        document = get_object_or_404(Document, id=document_id)  
        return render(request, 'documents/view_content.html', {'document': document})
    
    def view_document_description(request, document_id):
        document = get_object_or_404(Document, id=document_id)  # استرجاع المستند بناءً على المعرف
        return render(request, 'documents/view_description.html', {'document': document})

    def view_document_details(request, document_id):
        document = get_object_or_404(Document, id=document_id)  # استرجاع المستند بناءً على المعرف
        return render(request, 'documents/view_details.html', {'document': document})



@method_decorator(login_required, name='dispatch')
class DocumentListView(View):

    def get(self, request):
        documents = Document.objects.filter(is_private=False)

        if request.user.is_authenticated:
            private_docs = Document.objects.filter(uploaded_by=request.user, is_private=True)
            documents = documents | private_docs

        search_form = SearchForm()
        
        if 'query' in request.GET:
            search_form = SearchForm(request.GET)
            if search_form.is_valid():
                query = search_form.cleaned_data['query']
                documents = documents.filter(title__icontains=query)  

        valid_documents = [doc for doc in documents if doc.file]

        return render(request, 'documents/list.html', {'documents': valid_documents, 'search_form': search_form})
    def delete_document(request, document_id):
        document = get_object_or_404(Document, pk=document_id)
        if not document.has_access(request.user):
            return HttpResponseForbidden('You do not have permission to delete this document.')

        if document.file:
            file_path = document.file.path
            print(f"Deleting file: {file_path}")  
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except OSError as e:
                    print(f"Error deleting file: {e}")
            else:
                print(f"File '{file_path}' not found.")

        document.delete()
        return redirect('document_list')

    def download_document(request, document_id):
        document = get_object_or_404(Document, id=document_id)
        if not document.has_access(request.user):
            return HttpResponseForbidden('You do not have permission to delete this document.')
        mimetype, _ = mimetypes.guess_type(document.file.path)
        response = HttpResponse(document.file, content_type=mimetype)
        response['Content-Disposition'] = f'attachment; filename="{document.title}.{document.file.url.split(".")[-1]}"'
        return response
    

    def rename_document(request, document_id):
        document = get_object_or_404(Document, id=document_id)
        if not document.has_access(request.user):
            return HttpResponseForbidden('You do not have permission to delete this document.')
        if request.method == 'POST':
            new_title = request.POST.get('new_title')
            document.title = new_title
            document.save()
            return redirect('document_list')                
        return render(request, 'documents/rename_form.html', {'document': document})
    
    def replace_document(request, document_id):

        document = get_object_or_404(Document, id=document_id)
       
        if request.method == 'POST':
            form = DocumentReplaceForm(request.POST, request.FILES)
            if form.is_valid():
                file_path = document.file.path
                try:
                    os.remove(file_path)
                except OSError as e:
                     print(f"Error deleting file: {e}")
                new_document = form.save(commit=False)
                new_document.uploaded_by = request.user
                new_document.title = document.title 
                new_document.save()
                document.delete()
                return redirect('document_list')
        else:
            form = DocumentReplaceForm()
        return render(request, 'documents/replace_upload.html', {'form': form, 'document': document})
    
    def share_document(request, document_id):
        document = get_object_or_404(Document, id=document_id)
        if not document.has_access(request.user):
            return HttpResponseForbidden('You do not have permission to delete this document.')

        share_url = request.build_absolute_uri(reverse('download_document', args=[document_id]))
        context = {
            'document': document,
            'share_url': share_url,
        }
        return render(request, 'documents/share_document.html', context)

    def add_comment(request, document_id):
        document = get_object_or_404(Document, id=document_id)
        if not document.has_access(request.user):
            return HttpResponseForbidden('You do not have permission to delete this document.')
        if request.method == 'POST':
            comm = request.POST.get('comment')

            if comm:  # Validate if comment is not empty
                document.comment = comm
                document.save()  # Save the document with the new comment
                return redirect('document_list')

            else:  # Handle empty comment case
                error_message = "Please enter a comment."
                return render(request, 'documents/add_comment.html', {'document': document, 'error_message': error_message})

        return render(request, 'documents/add_comment.html', {'document': document})

    def edit_username(request, document_id):
        document = get_object_or_404(Document, id=document_id)

        if not document.has_access(request.user):
            return HttpResponseForbidden('You do not have permission to edit this document.')

        if request.method == 'POST':
            new_username = request.POST.get('new_username')
            user = document.uploaded_by  
            user.username = new_username
            user.clean_fields()
            user.save() 
            return redirect('document_list')

        return render(request, 'documents/edit_username.html', {'document': document})


@method_decorator(login_required, name='dispatch')
class DocumentGroupView(View):
    def create_document_group(request):
        if request.method == 'POST':
            form = DocumentGroupForm(request.POST)
            if form.is_valid():
                group = form.save()
                selected_document_ids = request.POST.getlist('documents')
                group.documents.set(selected_document_ids)  # Link documents to the group
                return redirect('view_document_group', group.id)
        else:
            form = DocumentGroupForm()

        documents = Document.objects.all()
        return render(request, 'documents/create_document_group.html', {'form': form, 'documents': documents})

    def view_document_group(request, group_id):
        group = get_object_or_404(DocumentGroup, id=group_id)
        return render(request, 'documents/view_document_group.html', {'group': group})

    def list_document_groups(request):
            groups = DocumentGroup.objects.all()  # استرجاع جميع المجموعات
            return render(request, 'documents/list_document_groups.html', {'groups': groups})
        
    def edit_document_group(request, group_id):
        group = get_object_or_404(DocumentGroup, id=group_id)
        if request.method == 'POST':
            form = DocumentGroupForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                selected_document_ids = request.POST.getlist('documents')
                group.documents.set(selected_document_ids)  # Link documents to the group
                return redirect('view_document_group', group.id)
        else:
            form = DocumentGroupForm(instance=group)

        documents = Document.objects.all()
        return render(request, 'documents/edit_document_group.html', {'form': form, 'documents': documents, 'group': group})

    def delete_document_group(request, group_id):
            """حذف مجموعة المستندات."""
            group = get_object_or_404(DocumentGroup, id=group_id)
            if request.method == 'POST':
                group.delete()
                return redirect('list_document_groups')  # إعادة التوجيه إلى قائمة المجموعات
            return render(request, 'documents/confirm_delete.html', {'group': group})
    

 
  

