from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado, name='listado'),
    path('<int:clase_id>/', views.detalle, name='detalle'),
]
