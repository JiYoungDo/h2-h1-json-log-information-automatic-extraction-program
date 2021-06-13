from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
   
    path('upload/', views.upload, name='upload'),
   
   # below is the key
    path('files/',views.file_list, name='file_list'),
    path('files/upload/', views.upload_file, name='upload_file'),
    path('files/<int:pk>/',views.delete_file,name='delete_file'),
    
    path('files/charts/',views.chart_template, name='show_chart'),
    
    path('class/files/',views.FileListView.as_view(), name='class_file_list'),
] 