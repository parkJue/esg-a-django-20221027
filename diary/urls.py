from django.urls import path
from diary import views

urlpatterns = [
    path('',views.index),
    path('<int:pk>/', views.detail),
    path('new/', views.new),
]
