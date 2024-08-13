# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.UserListView.as_view(), name='user_list'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('create-user/', views.AdminCreateUserView.as_view(), name='create_user'),
]
