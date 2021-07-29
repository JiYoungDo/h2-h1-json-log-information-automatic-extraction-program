
from django.conf import settings

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
   
    path('upload/', views.upload, name='upload'),
   
   # below is the key
    path('files/',views.file_list, name='file_list'),
    path('files/upload/', views.upload_file, name='upload_file'),
    path('files/<int:pk>/',views.delete_file,name='delete_file'),
    
    # path('files/charts/<int:pk>/<filegroup>/',views.show_chart, name='show_chart'),
    path('files/charts/<int:pk>/<filegroup>/',views.show_multi_chart, name='show_multi_chart'),
    

    path('class/files/',views.FileListView.as_view(), name='class_file_list'),

    # multichart 
    # path('files/charts/<int:pk>/<filegroup>/', views.show_multi_chart, name='show_multi_chart'),
] 
