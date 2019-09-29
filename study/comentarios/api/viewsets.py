from rest_framework import viewsets
from comentarios import models
from . import serializers

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = models.Comentario.objects.all()
    serializer_class = serializers.ComentariosSerializer
