from django.urls import path
from . import views
urlpatterns = [
    path('', views.nurse_list, name='nurse_list'),
    path('nurse/<int:pk>/', views.nurse_detail, name='nurse_detail'),
    path('nurse/new/', views.nurse_new, name='nurse_new'),
    path('nurse/<int:pk>/edit/', views.nurse_edit, name='nurse_edit'),
    path('nurse/<pk>/remove/', views.nurse_remove, name='nurse_remove'),
]