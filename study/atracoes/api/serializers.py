from rest_framework import serializers
from atracoes import models

class AtracoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Atracao
        fields = ('id','descricao','horario_funcionamento','idade_minima','foto')
