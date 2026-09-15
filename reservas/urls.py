from django.urls import path
from . import views

urlpatterns = [
    path('reservas/', views.listar),
    path('reservas/crear/', views.crear),
    path('reservas/<str:id>/actualizar/', views.actualizar),
    path('reservas/<str:id>/eliminar/', views.eliminar),
]
