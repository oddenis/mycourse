from django.urls import path
from .views import basket_add



urlpatterns = [
    path('basket_add/<int:course_id>', basket_add, name='basket_add' ),

]