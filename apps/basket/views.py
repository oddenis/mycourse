from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Basket, Line, Course
# Create your views here.



@login_required
def basket_add(request, course_id):
    user = request.user
    basket = Basket.objects.filter(owner=user, status=Basket.Status[0]).first()
    course = Course.objects.get(id=course_id)
    if not basket:
        basket = Basket.objects.create(owner=user)
        line = Line.objects.create(price = course.price)
        line.save()
    return render(request, 'basket/basket.html')