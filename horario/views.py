from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Clase, Reserva
from .serializers import ReservaSerializer


def listado(request):
    clases = Clase.objects.all()
    return render(request, 'horario/listado.html', {'clases': clases})


def detalle(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    return render(request, 'horario/detalle.html', {'clase': clase})


class ReservaViewSet(viewsets.ViewSet):

    def list(self, request):
        reservas = Reserva.objects()
        return Response(ReservaSerializer(reservas, many=True).data)

    def retrieve(self, request, pk=None):
        reserva = Reserva.objects(id=pk).first()
        if not reserva:
            return Response({'error': 'No encontrada'}, status=status.HTTP_404_NOT_FOUND)
        return Response(ReservaSerializer(reserva).data)

    def create(self, request):
        serializer = ReservaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reserva = Reserva(**serializer.validated_data).save()
        return Response(ReservaSerializer(reserva).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        reserva = Reserva.objects(id=pk).first()
        if not reserva:
            return Response({'error': 'No encontrada'}, status=status.HTTP_404_NOT_FOUND)
        Reserva.objects(id=pk).update(**request.data)
        return Response(ReservaSerializer(Reserva.objects(id=pk).first()).data)

    def destroy(self, request, pk=None):
        reserva = Reserva.objects(id=pk).first()
        if not reserva:
            return Response({'error': 'No encontrada'}, status=status.HTTP_404_NOT_FOUND)
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
