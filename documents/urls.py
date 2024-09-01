# documents/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.DocumentUploadView.as_view(), name='document_upload'),
    path('list/', views.DocumentListView.as_view(), name='document_list'),
    path('get-document/<str:pk>', views.GetDocumentView.as_view(), name='get-document'),
]
