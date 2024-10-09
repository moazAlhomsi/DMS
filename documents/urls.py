# documents/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.DocumentUploadView.as_view(), name='document_upload'),
    path('list/', views.DocumentListView.as_view(), name='document_list'),
    path('documents/<int:document_id>/delete/', views.DocumentListView.delete_document, name='document_delete'),
    path('documents/download/<int:document_id>/', views.DocumentListView.download_document, name='download_document'),
    path('rename/<int:document_id>/', views.DocumentListView.rename_document, name='rename_document'),
    path('edit_username/<int:document_id>/', views.DocumentListView.edit_username, name='edit_username'),
    path('replace/<int:document_id>/', views.DocumentListView.replace_document, name='replace_document'),
    path('share/<int:document_id>/', views.DocumentListView.share_document, name='share_document'),
    path('document/<int:document_id>/content/',views.DocumentUploadView.view_document_content, name='view_document_content'),
    path('document/<int:document_id>/description/', views.DocumentUploadView.view_document_description, name='view_document_description'),
    path('document/<int:document_id>/detalis/', views.DocumentUploadView.view_document_details, name='view_document_details'),


    path('add_comment/<int:document_id>/', views.DocumentListView.add_comment, name='add_comment'),
    path('create-group/', views.DocumentGroupView.create_document_group, name='create_document_group'),
    path('group/<int:group_id>/', views.DocumentGroupView.view_document_group, name='view_document_group'),
    path('groups/', views.DocumentGroupView.list_document_groups, name='list_document_groups'),
    path('edit-group/<int:group_id>/', views.DocumentGroupView.edit_document_group, name='edit_document_group'),
    path('document-group/<int:group_id>/delete/', views.DocumentGroupView.as_view(), name='delete_document_group'),








]

    # path('describe/<int:document_id>/', views.DocumentListView.describe_image, name='describe_image'),

