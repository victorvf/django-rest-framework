from rest_framework import serializers
from localizacao import models

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = ('id','referencia_um','referencia_dois','cidade','estado','pais','latitude','longitude')
