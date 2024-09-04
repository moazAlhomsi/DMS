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

    # holidays allocated by admin to employees
    path('holidays/' , views.ListHolidaysView.as_view() , name="holidays_list"),
    path('create-holiday/' , views.CreateHolidayView.as_view() , name="create_holiday"),
    path('holiday-info/<str:pk>' , views.UpdateHolidayView.as_view() , name="holiday_info"),
    path('delete-holiday/<str:pk>' , views.DeleteHolidayView.as_view() , name="delete_holiday"),

    # employee's absences without permission by admin
    path('absences/' , views.ListAbsenceView.as_view() , name="absences_list"),
    path('create-absence/' , views.CreateAbsenceView.as_view() , name="create_absence"),
    path('absence-info/<str:pk>' , views.UpdateAbsenceView.as_view() , name="absence_info"),
    path('delete-absence/<str:pk>' , views.DeleteAbsenceView.as_view() , name="delete_absence"),
]
