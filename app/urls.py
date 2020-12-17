from django.urls import path, include
from .views import home, contacto, galeria, agregar_producto, listar_productos,\
     modificar_producto, eliminar_producto, registro, ProductoViewset, error_facebook, salir
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto',ProductoViewset)
#localhost:8000/api/producto
urlpatterns = [
    path('' , home , name ="home"),
    path('contacto/', contacto, name = "contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar_producto/',agregar_producto,name="agregar_producto"),
    path('listar_productos/',listar_productos,name="listar_productos"),
    path('modificar_producto/<id>/',modificar_producto,name="modificar_producto"),
    path('eliminar_producto/<id>/',eliminar_producto,name="eliminar_producto"),
    path('registro/',registro,name="registro"),
    path('api/',include(router.urls)),
    path('error_facebook/',error_facebook,name="error_facebook"),
    path('salir/',salir, name='salir'),
]
