from rest_framework import serializers
from comentarios import models

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comentario
        fields = ('id','usuario','comentario','data','aprovado')
