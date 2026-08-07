from django.shortcuts import render
from django.http import Http404
from .data import clases

def listado(request):
    return render(request, 'horario/listado.html', {'clases': clases})


def detalle(request, clase_id):

    clase = next((clase for clase in clases if clase["id"] == clase_id), None)
    if clase is None:
        raise Http404("Clase no encontrada")
    return render(request, 'horario/detalle.html', {'clase': clase})
    


