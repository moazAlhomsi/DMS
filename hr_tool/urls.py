# pr_tool/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('employees/' , views.ListEmployeesView.as_view() , name="employee_list"),
    path('create-employee/' , views.CreateEmployeeView.as_view() , name="create_employee"),
    path('employee-profile/<str:pk>' , views.UpdateEmployeeView.as_view() , name="employee_profile"),
    path('delete-employee/<str:pk>' , views.DeleteEmployeeView.as_view() , name="delete_employee"),

    path('salaries/' , views.ListSalariesView.as_view() , name="salary_list"),
    path('create-salary/' , views.CreateSalaryView.as_view() , name="create_salary"),
    path('salary-info/<str:pk>' , views.UpdateSalaryView.as_view() , name="salary_info"),
    path('delete-salary/<str:pk>' , views.DeleteSalaryView.as_view() , name="delete_salary"),

    path('days-off/' , views.ListDaysOffView.as_view() , name="days_off_list"),
    path('create-day-off/' , views.CreateDayOffView.as_view() , name="create_day_off"),
    path('day-off-info/<str:pk>' , views.UpdateDayOffView.as_view() , name="day_off_info"),
    path('delete-day-off/<str:pk>' , views.DeleteDayOffView.as_view() , name="delete_day_off"),
]
