from django.shortcuts import render, get_object_or_404
from .models import Course, Category


def main(request):
    courses = Course.objects.all()
    category = Category.objects.all()
    return render(request, 'main.html', {'courses':courses, 'categories':category})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'category/detail.html', {'active_category':category})


def course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course/detail.html', {'course':course})