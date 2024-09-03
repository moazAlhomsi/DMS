# hr_tool/views.py

from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Employee , Salary , Holiday
from .forms import EmployeeRegistrationForm , EmployeeUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from django.views.generic import ListView , DeleteView , CreateView , UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ListEmployeesView(ListView):
    model = Employee
    template_name = 'hr_tool/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 5





# @method_decorator(login_required, name='dispatch')
# class CreateEmployeeView(View):
#     def get(self,request):
#         form = EmployeeRegistrationForm()
#         return render(request , 'hr_tool/create_employee.html' , context={'form':form})
    
#     def post(self,request):
#         form = EmployeeRegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create(
#                 username = form.cleaned_data['username'],
#                 email = form.cleaned_data['email'],
#             )
#             user.set_password(form.cleaned_data['password1'])
#             Employee.objects.create(
#                 user=user,
#                 department=form.cleaned_data['department'],
#                 position=form.cleaned_data['position']
#             )
#             return redirect('employee_list')
#         return redirect('create_employee')




class CreateEmployeeView(CreateView):
    model = Employee
    form_class = EmployeeRegistrationForm
    template_name = 'hr_tool/create_employee.html'
    success_url = '/hr/employees/'
    



@method_decorator(login_required, name='dispatch')
class DeleteEmployeeView(DeleteView):
    model = Employee
    template_name = 'hr_tool/delete_employee.html'
    context_object_name = 'employee'
    success_url = '/hr/employees/'
    
    

@method_decorator(login_required, name='dispatch')
class UpdateEmployeeView(UpdateView):
    model = Employee
    template_name = 'hr_tool/employee_profile.html'
    form_class = EmployeeUpdateForm
    success_url = '/hr/employees/'

    # add extra data for each employee in the context
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        holidays = Holiday.objects.filter(employee=self.object).count() # get number of days off for the employee
        context['holidays'] = holidays 
        return context



@method_decorator(login_required, name='dispatch')
class CreateSalaryView(CreateView):
    model = Salary
    fields = '__all__'
    template_name = 'hr_tool/create_salary.html'
    success_url = '/hr/salaries/'


@method_decorator(login_required, name='dispatch')
class ListSalariesView(ListView):
    model = Salary
    template_name = 'hr_tool/salaries.html'
    context_object_name = 'salaries'
    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class UpdateSalaryView(UpdateView):
    model = Salary
    fields = '__all__'
    template_name = 'hr_tool/salary_info.html'
    success_url = '/hr/salaries/'


@method_decorator(login_required, name='dispatch')
class DeleteSalaryView(DeleteView):
    model = Salary
    template_name = 'hr_tool/delete_salary.html'
    context_object_name = 'salary'
    success_url = '/hr/salaries/'



@method_decorator(login_required, name='dispatch')
class CreateHolidayView(CreateView):
    model = Holiday
    fields = '__all__'
    template_name = 'hr_tool/create_holiday.html'
    success_url = '/hr/holidays/'


@method_decorator(login_required, name='dispatch')
class ListHolidaysView(ListView):
    model = Holiday
    template_name = 'hr_tool/holiday.html'
    context_object_name = 'holidays'
    paginate_by = 5


@method_decorator(login_required, name='dispatch')
class UpdateHolidayView(UpdateView):
    model = Holiday
    fields = '__all__'
    template_name = 'hr_tool/holiday_info.html'
    success_url = '/hr/holidays/'
    context_object_name = 'holiday'


@method_decorator(login_required, name='dispatch')
class DeleteHolidayView(DeleteView):
    model = Holiday
    template_name = 'hr_tool/delete_holiday.html'
    context_object_name = 'holiday'
    success_url = '/hr/holidays/'

