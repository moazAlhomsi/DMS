from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator , MaxValueValidator
User = get_user_model()

# Create your models here.


class Employee(User):
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self) -> str:
        return self.username
    


class Holiday(models.Model):
    DAYOFF_CHOICES = (
        ('Full Day','8 Hours'),
        ('Half Day','4 Hours'),
    )
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    hours = models.CharField(choices=DAYOFF_CHOICES , max_length=40)
    start = models.DateField()
    end = models.DateField()

    def __str__(self) -> str:
        return f'{self.employee.username} - {self.hours}'



class Absence(models.Model):
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    days = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(1000)])
    start = models.DateField()
    end = models.DateField()

    def __str__(self) -> str:
        return f'{self.employee.username} - {self.days}'



class Salary(models.Model):
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.employee.username}-{self.amount}'
    



# class UpfrontPayment(models.Model):
#     pass



# class Absence(models.Model):
#     pass