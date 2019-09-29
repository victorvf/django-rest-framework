from rest_framework import viewsets
from avaliacoes import models
from . import serializers

class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = models.Avaliacao.objects.all()
    serializer_class = serializers.AvaliacoesSerializer
