
"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('parroquia/<int:id>', views.getParroquia,
            name='getParroquia'),
        path('crear/parroquia', views.setParroquia,
            name='setParroquia'),
        path('editar/parroquia/<int:id>', views.editParroquia,
            name='editParroquia'),
        path('crear/barrioParroquia/<int:id>', views.setBarrioParroquia,
            name='setBarrioParroquia'),
        path('crear/barrio', views.setBarrio,
            name='setBarrio'),
        path('editar/barrio/<int:id>', views.editBarrio,
            name='editBarrio'),
        
]