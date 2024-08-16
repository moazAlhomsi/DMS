# users/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .forms import UserRegistrationForm, UserUpdateForm, AdminChangePasswordForm ,UserLoginForm # UserLoginForm will not be used in this snippet
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()




class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    paginate_by = 2  # set pagination to an appropriate number

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
class LogoutView(View):
    def get(self,request):
        if request.user:
            logout(request)
            return redirect('login')
        else:
            return HttpResponse('you are not logged in')





@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def get(self, request,user_id):
        try:
            user = User.objects.get(id=user_id)
            form = UserUpdateForm(instance=user)
        except User.DoesNotExist:
            return HttpResponse('user does not exist')
        return render(request, 'users/profile.html', {'form': form,'user':user})
    
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def post(self, request,user_id):
        user = User.objects.get(id=user_id)
        form = UserUpdateForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Or redirect to a user management page
        return render(request, 'users/profile.html', {'form': form})




@method_decorator(login_required, name='dispatch')
class DeleteUserView(View):
    def post(self,request,user_id):
        try:
            User.objects.get(id=user_id).delete()
            return redirect('user_list')
        except User.DoesNotExist:
            return HttpResponse('user does not exist')




@method_decorator(login_required, name='dispatch')
class PerformActionView(View):
    def post(self,request):
        selected_items = request.POST.getlist('selected_users')
        users = User.objects.filter(id__in=selected_items)

        # perform DB operation depending on the chosen action
        if request.POST.get('action') == 'delete':
            users.delete()
        elif request.POST.get('action') == 'activate':
            users.update(is_active=True)
        elif request.POST.get('action') == 'deactivate':
            users.update(is_active=False)
        return redirect('user_list')
        


@method_decorator(login_required, name='dispatch')
class AdminChangePasswordView(View):
    @method_decorator(user_passes_test(lambda u: u.role=='Admin'))
    def get(self,request,user_id):
        form = AdminChangePasswordForm()
        return render(request,'users/change_password.html',{'form':form})
    
    @method_decorator(user_passes_test(lambda u: u.role=='Admin'))
    def post(self,request,user_id):
        form = AdminChangePasswordForm(request.POST)
        try:
            user = User.objects.get(pk=user_id)
            # if the form is valid and the passwords match then set a new password
            if form.is_valid():
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                return redirect('profile', user_id=user_id)
        except User.DoesNotExist:
            return HttpResponse("User does not exist")
