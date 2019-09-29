from rest_framework import viewsets
from atracoes import models
from . import serializers

class AtracoesViewSet(viewsets.ModelViewSet):
    queryset = models.Atracao.objects.all()
    serializer_class = serializers.AtracoesSerializer
