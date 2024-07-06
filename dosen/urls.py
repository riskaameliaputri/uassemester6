from django.urls import path
from . import views

urlpatterns = [
    path('dosen/', views.dosen_list, name='dosen-list'),
    path('dosen/<int:pk>/', views.dosen_detail, name='dosen-detail'),
]
