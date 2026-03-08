from django.urls import path
from . import views


urlpatterns = [

    path("", views.home, name="home"),
    
    path("", views.lista_detentos, name="home"),

    path("detentos/", views.lista_detentos, name="lista_detentos"),

    path("detento/<int:detento_id>/", views.detalhe_detento, name="detalhe_detento"),

    path("consulta/", views.consulta_detento, name="consulta_detento"),
    
]