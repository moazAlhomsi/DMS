from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator , MaxValueValidator
User = get_user_model()

# Create your models here.


class Employee(User):
    POSITION_CHOICES = (
        ('Intern','Intern'),
        ('Full-Time','Full-Time'),
        ('Part-Time','Part-Time'),
    )
    DEPARTMENT_CHOICES = (
        ('HR','HR'),
        ('Finance','Finance'),
    )
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, default='Full-Time')
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, default='HR')

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self) -> str:
        return self.username
    


class Holiday(models.Model):
    HOLIDAY_CHOICES = (
        ('Full Day','8 Hours'),
        ('Half Day','4 Hours'),
    )
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    hours = models.CharField(choices=HOLIDAY_CHOICES , max_length=40)
    start = models.DateField()
    end = models.DateField()

    def __str__(self) -> str:
        return f'{self.employee.username} - {self.hours}'



class Absence(models.Model):
    ABSENCES_CHOICES = (
        ('Sick Leave','Sick Leave'),
        ('_','_'),
    )
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    days = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(1000)])
    reason = models.CharField(max_length=100, choices=ABSENCES_CHOICES,default='_')
    start = models.DateField()
    end = models.DateField()

    def __str__(self) -> str:
        return f'{self.employee.username} - {self.days}'




class Recruitment(models.Model):
    POSITION_CHOICES = (
        ('Intern','Intern'),
        ('Full-Time','Full-Time'),
        ('Part-Time','Part-Time'),
    )
    STATE_CHOICES = (
        ('Done','Done'),
        ('Review','Review'),
        ('Initial','Initial'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    state = models.CharField(max_length=30 , choices=STATE_CHOICES)
    image = models.ImageField(upload_to='recruiters/images', default='placeholder.jpg')
    position = models.CharField(max_length=100 , choices=POSITION_CHOICES,default='Initial')
    department = models.CharField(max_length=100)
    resume = models.FileField(upload_to='recruitment/resumes',blank=True,null=True)




class Skill(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



class WorkGoal(models.Model):
    PROGRESS_CHOICES = (
        ('0%','0%'),
        ('25%','25%'),
        ('50%','50%'),
        ('75%','75%'),
        ('100%','100%'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill , on_delete=models.CASCADE) # modify the on_delete
    created = models.DateField(auto_now_add=True)
    progress = models.CharField(max_length=20 , choices=PROGRESS_CHOICES ,default="0%")

    def __str__(self) -> str:
        return f"{self.employee.username} - {self.skill}"
