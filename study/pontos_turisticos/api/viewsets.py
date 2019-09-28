from pontos_turisticos import models
from rest_framework import viewsets
from . import serializers

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    queryset = models.PontoTuristico.objects.all()
    serializer_class = serializers.PontoTuristicoSerializer
