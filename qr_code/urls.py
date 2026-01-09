from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('download/<str:filename>/', views.download_qr, name="download_qr"),
    path('delete-all/', views.delete_all_qrs, name="delete_all_qrs")
]
