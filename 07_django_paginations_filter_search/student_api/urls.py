from django.urls import path, include

from rest_framework import routers

from .views import home, ogrencileri_listele, ogrenci_olustur, ozel_ogrenci_detay_goruntuleme, var_olan_ozel_obje_yenile, ogrenc_sil, StudentListCreate, StudentDetail, StudentGAV, StudentDetailGAV, StudentCV, StudentDetailCV, StudentMVS, PathMVS

router = routers.DefaultRouter()
router.register("stundetmvs", StudentMVS)  # stundent/ stundent/<int:pk>/ 
router.register("pathmvs", PathMVS)  # stundent/ stundent/<int:pk>/ 


urlpatterns = [
    # FBV
    path("home/", home),
    path("students/", ogrencileri_listele),
    path("students/create/", ogrenci_olustur),
    path("students/<int:pk>/", ozel_ogrenci_detay_goruntuleme),
    path("student/update/<int:pk>/", var_olan_ozel_obje_yenile),
    path("student/delete/<int:pk>/", ogrenc_sil),

    # CBV
    path("student/", StudentListCreate.as_view()),
    path("student/<int:pk>/", StudentDetail.as_view()),

    path("studentgap/", StudentGAV.as_view()),
    path("studentgap/<int:id>/", StudentDetailGAV.as_view()),
    path("studentcv/", StudentCV.as_view()),
    path("studentcv/<int:pk>/", StudentDetailCV.as_view()),


    # path("", include(router.urls))

] + router.urls
