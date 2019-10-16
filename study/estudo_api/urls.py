from django.contrib import admin
from django.urls import path, include

##### config media #############
from django.conf import settings
from django.conf.urls.static import static
###############################

############## django rest ######################
from rest_framework import routers
from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet
from comentarios.api.viewsets import ComentariosViewSet
from localizacao.api.viewsets import LocalizacaoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, base_name='PontoTuristico')
router.register(r'atracoes', AtracoesViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'localizacao', LocalizacaoViewSet)
#################################################

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
