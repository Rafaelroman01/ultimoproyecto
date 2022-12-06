from django.urls import path
from Appcoder.views import *

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("participantes/", participantes, name="coder-participantes"),
    path("recreadores/", recreadores, name="coder-recreadores"),
    path("recreadores/crear/", creacion_recreadores, name="coder-recreadores-crear"),
    path("excursiones/", excursiones, name="coder-excursiones"),
    path("excursiones/borrar/id/", eliminar_excursion, name="coder-excursiones-borrar"),
    path("excursiones/buscar/", buscar_excursion, name="coder-excursiones-buscar"),
    path("excursiones/buscar/resultados/", resultados_busqueda_excursion, name="coder-excursiones-buscar-resultados"),
    path("documentacion/", documentacion, name="coder-documentacion"),
    
]
