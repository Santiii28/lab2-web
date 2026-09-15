import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Reserva


# CREATE
@csrf_exempt
def crear(request):
    datos = json.loads(request.body)
    reserva = Reserva(**datos).save()
    return JsonResponse({'id': str(reserva.id)})


# READ
def listar(request):
    reservas = Reserva.objects()
    return JsonResponse(
        [{'id': str(r.id), 'nombre_miembro': r.nombre_miembro, 'clase': r.clase, 'fecha': r.fecha} for r in reservas],
        safe=False,
    )


# UPDATE
@csrf_exempt
def actualizar(request, id):
    datos = json.loads(request.body)
    Reserva.objects(id=id).update(**datos)
    return JsonResponse({'ok': True})


# DELETE
@csrf_exempt
def eliminar(request, id):
    Reserva.objects(id=id).delete()
    return JsonResponse({'ok': True})
