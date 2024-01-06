from django.urls import path

from .views import home, list_students, create_student, display_special_student_details,refresh_object, delete_student

urlpatterns = [
    path('home/', home),
    path('students/', list_students),
    path('students/create/', create_student),
    path('students/<int:pk>/', display_special_student_details),
    path('students/update/<int:pk>/', refresh_object),
    path('students/delete/<int:pk>/', delete_student),
]
