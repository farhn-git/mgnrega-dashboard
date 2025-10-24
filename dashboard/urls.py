from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('district/', views.district_view, name='district'),
    path('run-migrations/', views.run_migrations),
]