from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),

    path('files/',views.file_list, name='file_list'),
    path('files/upload/', views.upload_file, name='upload_file'),
] 