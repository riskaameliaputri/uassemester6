from django.urls import path
from . import views

urlpatterns = [
    path('mahasiswa/', views.mahasiswa_list, name='mahasiswa-list'),
    path('mahasiswa/<int:pk>/', views.mahasiswa_detail, name='mahasiswa-detail'),
]
