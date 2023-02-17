from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.landing,name='dashboard_url'),
    path('delete/', views.delete_files, name='delete_files'),
    path('result/', views.result_images, name='result_url'),
 ]
