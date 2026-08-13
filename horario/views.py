from django.shortcuts import render, get_object_or_404
from .models import Clase


def listado(request):
    clases = Clase.objects.all()
    return render(request, 'horario/listado.html', {'clases': clases})


def detalle(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    return render(request, 'horario/detalle.html', {'clase': clase})
