from django.db import models
from django.contrib.auth import get_user_model
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
    


class DayOff(models.Model):
    DAYOFF_CHOICES = (
        ('Full Day','8 Hours'),
        ('Half Day','4 Hours'),
    )
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    amount = models.CharField(choices=DAYOFF_CHOICES , max_length=40)
    start = models.DateField()
    end = models.DateField()



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