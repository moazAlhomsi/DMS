# pr_tool/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hr/' , views.MainHR.as_view() , name="hr"),

    path('employees/' , views.ListEmployeesView.as_view() , name="employee_list"),
    path('create-employee/' , views.CreateEmployeeView.as_view() , name="create_employee"),
    path('employee/<str:pk>' , views.UpdateEmployeeView.as_view() , name="employee_profile"),
    path('delete-employee/<str:pk>' , views.DeleteEmployeeView.as_view() , name="delete_employee"),

    # holidays allocated by admin to employees
    path('holidays/' , views.ListHolidaysView.as_view() , name="holidays_list"),
    path('create-holiday/' , views.CreateHolidayView.as_view() , name="create_holiday"),
    path('holiday/<str:pk>' , views.UpdateHolidayView.as_view() , name="holiday_info"),
    path('delete-holiday/<str:pk>' , views.DeleteHolidayView.as_view() , name="delete_holiday"),

    # employee's absences with/without reason by admin
    path('absences/' , views.ListAbsenceView.as_view() , name="absences_list"),
    path('create-absence/' , views.CreateAbsenceView.as_view() , name="create_absence"),
    path('absence/<str:pk>' , views.UpdateAbsenceView.as_view() , name="absence_info"),
    path('delete-absence/<str:pk>' , views.DeleteAbsenceView.as_view() , name="delete_absence"),

    # Recruitment to store info about recruiters and thier interview process
    path('recruiters/' , views.ListRecruitersView.as_view() , name="recruiters_list"),
    path('recruiter/<str:pk>/delete' , views.DeleteRecruiterView.as_view() , name="recruiters_list"),
    path('recruiter/form' , views.CreateRecruiterView.as_view() , name="recruiters_list"),

    # Development Tracking
    path('goals/' , views.ListGoalsView.as_view() , name="goals_list"),
    path('goals/new' , views.CreateGoalView.as_view() , name="create_goal"),
    path('goals/<str:pk>/delete' , views.DeleteGoalView.as_view() , name="delete_goal"),
    path('skills/' , views.ListSkillsView.as_view() , name="skills_list"),
    path('skills/new' , views.CreateSkillView.as_view() , name="create_skill"),
    path('skills/<str:pk>/delete' , views.DeleteSkillView.as_view() , name="delete_skill"),

    

]
