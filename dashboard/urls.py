from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('district/', views.district_view, name='district'),
    path('load-records/', views.load_records),
    path('sync-data/', views.sync_data),
]