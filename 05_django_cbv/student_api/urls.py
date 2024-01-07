from django.urls import path, include

from rest_framework import routers

from .views import home, list_students, create_student, display_special_student_details,refresh_object, delete_student, StudentListCreate, StudentDetail, StudentGAV, StudentDetailGAV, StudentCV, StudentDetailCV, StudentMVS, PathMVS



router = routers.DefaultRouter()
router.register('studentmvs', StudentMVS) # student/ student/<int:pk>/
router.register('pathmvs', PathMVS) # student/ path/<int:pk>/

urlpatterns = [
    # FBV
    path('home/', home),
    path('students/', list_students),
    path('students/create/', create_student),
    path('students/<int:pk>/', display_special_student_details),
    path('students/update/<int:pk>/', refresh_object),
    path('students/delete/<int:pk>/', delete_student),


    # CBV
    path("student/", StudentListCreate.as_view()),
    path("student/<int:pk>/", StudentDetail.as_view()),

    path("studentgap/", StudentGAV.as_view()),
    path("studentgap/<int:pk>/", StudentDetailGAV.as_view()),
    path("studentcv/<int:pk>/", StudentCV.as_view()),
    path("studentdcv/<int:pk>/", StudentDetailCV.as_view()),


    # path("", include(router.urls))

] + router.urls
