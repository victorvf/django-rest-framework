from rest_framework import serializers
from pontos_turisticos import models

class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PontoTuristico
        fields = ('id','nome','descricao','foto')
