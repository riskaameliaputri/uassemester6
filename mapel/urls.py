from django.urls import path
from . import views

urlpatterns = [
    path('mapel/', views.mapel_list, name='mapel-list'),
    path('mapel/<int:pk>/', views.mapel_detail, name='mapel-detail'),
]
