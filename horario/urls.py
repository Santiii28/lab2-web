from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado, name='listado'),
    path('<int:clase_id>/', views.detalle, name='detalle'),
    path('reservas/', views.listar_reservas),
    path('reservas/crear/', views.crear_reserva),
    path('reservas/<str:id>/actualizar/', views.actualizar_reserva),
    path('reservas/<str:id>/eliminar/', views.eliminar_reserva),
]