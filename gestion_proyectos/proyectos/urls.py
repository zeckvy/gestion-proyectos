from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_proyectos, name='lista_proyectos'),
    path('crear/', views.crear_proyecto, name='crear_proyecto'),
    path('proyecto/<int:id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyecto/<int:id>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
]