from django.urls import path

from . import views

urlpatterns = [
    path('<int:val>/', views.index, name="index"),
    path('upload/', views.upload_file, name="upload"),
    path('test/', views.test_single_pg, name="test")
]
