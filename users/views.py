# users/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .forms import UserRegistrationForm, UserLoginForm # UserLoginForm will not be used in this snippet
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()

class AdminCreateUserView(View):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'users/admin_create_user.html', {'form': form})

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Or redirect to a user management page
        return render(request, 'users/admin_create_user.html', {'form': form})



class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        email = request.POST.get('username')  # Get email from the username field
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)  # Get user by email
            user = authenticate(request, username=user.username, password=password)  # Authenticate with username
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
            else:
                form = AuthenticationForm(request, data=request.POST)
                form.add_error(None, "Invalid email or password")
        except User.DoesNotExist:
            form = AuthenticationForm(request, data=request.POST)
            form.add_error(None, "Invalid email or password")

        return render(request, 'users/login.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        return render(request, 'users/profile.html')
