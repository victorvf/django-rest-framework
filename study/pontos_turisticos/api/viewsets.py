from pontos_turisticos import models
from rest_framework import viewsets
from . import serializers

class PontoTuristicoViewSet(viewsets.ModelViewSet):

    #queryset = models.PontoTuristico.objects.all() se eu quiser fazer mais de um filtro, eu tenho que usar o get_queryset
    serializer_class = serializers.PontoTuristicoSerializer

    def get_queryset(self):
        return models.PontoTuristico.objects.filter(aprovado=True)

    #Basicamente para fazer o override dos verbos GET, POST, DELETE ..., eu chamo as funcões a baixo:
    #def list(self, request, *args, **kwargs): <-- a lista como um todo
    #def create(self, request, *args, **kwargs):
    #def destroy(self, request, *args, **kwargs):
    #def retrieve(self, request, *args, **kwargs): <-- recurso isolado
    #def update(self, request, *args, **kwargs):
    #def partial_update(self, request, *args, **kwargs):

    #propria action, detail=True para que o framework me passe a pk
    #@action(methods=['GET','POST'], detail=True)
    #def denunciar(self, request, pk=None):
