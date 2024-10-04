# pr_tool/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hr/' , views.MainHR.as_view() , name="hr"),

    path('employees/' , views.ListEmployeesView.as_view() , name="employee_list"),
    path('create-employee/' , views.CreateEmployeeView.as_view() , name="create_employee"),
    path('employee-profile/<str:pk>' , views.UpdateEmployeeView.as_view() , name="employee_profile"),
    path('delete-employee/<str:pk>' , views.DeleteEmployeeView.as_view() , name="delete_employee"),

    # holidays allocated by admin to employees
    path('holidays/' , views.ListHolidaysView.as_view() , name="holidays_list"),
    path('create-holiday/' , views.CreateHolidayView.as_view() , name="create_holiday"),
    path('holiday-info/<str:pk>' , views.UpdateHolidayView.as_view() , name="holiday_info"),
    path('delete-holiday/<str:pk>' , views.DeleteHolidayView.as_view() , name="delete_holiday"),

    # employee's absences with/without reason by admin
    path('absences/' , views.ListAbsenceView.as_view() , name="absences_list"),
    path('create-absence/' , views.CreateAbsenceView.as_view() , name="create_absence"),
    path('absence-info/<str:pk>' , views.UpdateAbsenceView.as_view() , name="absence_info"),
    path('delete-absence/<str:pk>' , views.DeleteAbsenceView.as_view() , name="delete_absence"),

    # Recruitment to store info about recruiters and thier interview process
    path('recruiters/' , views.ListRecruitersView.as_view() , name="recruiters_list"),
    # path('reccruiter-info/<str:pk>' , views.GetRecruiterView.as_view() , name="absence_info"),

    # Development Tracking
    

]
