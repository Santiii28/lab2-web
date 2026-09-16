from rest_framework import serializers


class ReservaSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    nombre_miembro = serializers.CharField()
    clase = serializers.CharField()
    fecha = serializers.CharField()
