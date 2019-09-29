from rest_framework import viewsets
from localizacao import models
from . import serializers

class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = models.Endereco.objects.all()
    serializer_class = serializers.LocalizacaoSerializer
