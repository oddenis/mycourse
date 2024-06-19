from django.db import models
from apps.profiles.models import User
from apps.course.models import Course
# Create your models here.



class Basket(models.Model):
    Status= [('OPEN','open'),
                ('CLOSE' , 'close')]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='baskets')
    status = models.CharField(choices=Status, default=Status[0], max_length=20)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.owner


class Line(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_lines')